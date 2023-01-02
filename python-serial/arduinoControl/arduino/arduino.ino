void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  if (Serial.available() > 0)
  {
      char c= Serial.read();
      if(c=='1')
      {
        digitalWrite(13,HIGH);
      }
      else if(c=='2')
      {
        digitalWrite(13,LOW);
      }
  }

}