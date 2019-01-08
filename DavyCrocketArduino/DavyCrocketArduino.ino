char receivedChar;
boolean newData = false;
const int speedPin = 9;
const int dirPin = 6;
int speedVar = 1;

void setup() {
 Serial.begin(9600);
 pinMode(speedPin, OUTPUT);
 pinMode(dirPin, OUTPUT);
 analogWrite(speedPin, 0);
 analogWrite(dirPin, 0);
 Serial.println("<Arduino is ready>");
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
 if (receivedChar == 'l') {
    Serial.println("moving left.");
    analogWrite(dirPin, 255);
    analogWrite(speedPin, 1);
    delay(75);
    analogWrite(speedPin, 0);
  } else if (receivedChar == 'r') {
    Serial.println("moving right.");
    analogWrite(dirPin, 0);
    analogWrite(speedPin, 1);
    delay(75);
    analogWrite(speedPin, 0);
  }
}



