char receivedChar;
boolean newData = false;
const int stepPin = 9;
const int dirPin = 6;
int speedVar = 1000;

void setup() {
 Serial.begin(9600);
 pinMode(stepPin, OUTPUT);
 pinMode(dirPin, OUTPUT);
 digitalWrite(stepPin, LOW);
 digitalWrite(dirPin, LOW);
}

void loop() {
 recvOneChar();
 showNewData();
}

void recvOneChar() {
 if (Serial.available() > 0) {
 receivedChar = Serial.read();
 newData = true;
 }
}

void showNewData() {
 if (newData == true) {
 moveAntennas();
 newData = false;
 }
}

void moveAntennas() {
 if (receivedChar == 'r') {
    digitalWrite(dirPin, HIGH);
    digitalWrite(stepPin, HIGH);
    delay(1000);
    digitalWrite(stepPin, LOW);
  } else if (receivedChar == 'l') {
    digitalWrite(dirPin, LOW);
    digitalWrite(stepPin, HIGH);
    delay(1000);
    digitalWrite(stepPin, LOW);
  }
}



