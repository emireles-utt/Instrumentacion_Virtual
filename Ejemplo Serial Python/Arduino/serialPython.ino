uint8_t datoSerie;
uint16_t valAdc;

void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  pinMode(8, INPUT_PULLUP);
}

void loop(){
  if(Serial.available() > 0){
    datoSerie = Serial.read();
    switch(datoSerie){
      case 'A':
        digitalWrite(13, HIGH);
        break;
      
      case 'a':
        digitalWrite(13, LOW);
        break;
      
      case '1':
        Serial.print(digitalRead(8));
        break;
      
      case 'H':
        valAdc = analogRead(A0);
        Serial.println(valAdc);
        break;
    }
  }
}
