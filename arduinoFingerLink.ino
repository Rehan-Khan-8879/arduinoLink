void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    int val = Serial.parseInt();
    if(val == 1){
      digitalWrite(2,HIGH);
    }else if(val == 2){
      digitalWrite(3,HIGH);
    }else if(val == 3){
      digitalWrite(4,HIGH);
    }else if(val == 4){
      digitalWrite(5,HIGH);
    }else if(val == 5){
      digitalWrite(6,HIGH);
    }else if(val == 0){
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
    }
  }
}
