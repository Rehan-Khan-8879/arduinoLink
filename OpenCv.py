import cv2
import serial
import time
import mediapipe as mp

#settingup Serial communication
arduino = serial.Serial(port='COM2',baudrate=9600,timeout=1)
# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Define the landmarks for finger tips
finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
thumb_tip = 4

# Start capturing video
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip horizontally for natural interaction
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            landmarks = hand_landmarks.landmark

            # Count raised fingers
            fingers_up = 0

            # Check each finger tip
            for tip in finger_tips:
                # Compare the tip's y-coordinate with the middle knuckle
                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers_up += 1

            # Check thumb separately (horizontal movement)
            if landmarks[thumb_tip].x < landmarks[thumb_tip - 1].x:
                fingers_up += 1

            # Display the number of raised fingers
            cv2.putText(frame, f'Fingers: {fingers_up}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(fingers_up)  # Print to console

            temp = str(fingers_up) + '\n'
            arduino.write(temp.encode())


            

    


    # Display the frame
    cv2.imshow('Finger Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()