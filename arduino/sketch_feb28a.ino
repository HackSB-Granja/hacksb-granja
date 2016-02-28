
#include <Servo.h>

int a = 0;
int angle = 180;
Servo servo; 

void setup() {
  // put your setup code here, to run once:
  servo.attach(9);
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(3000);
  Serial.println("Leyendo");
    if(Serial.available()){

      String com = Serial.readString();
      String logg = "Execute " + com;
      Serial.println(logg);
      if(com.startsWith("#open")){
        open();
      }else if(com.startsWith("#close")){
        close();
      }
    }

}

void open() {
  Serial.println("Abriendo");
  /*for(angle=180;angle > 0;angle--){
    servo.write(angle);
    delay(15);*/
  }


void close() {
  Serial.println("Cerando");
  /*for(angle=0;angle <180;angle++){
    servo.write(angle);
    delay(15);*/
  }


