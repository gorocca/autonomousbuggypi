#include<Servo.h>
//Declaracion de variables
Servo ESC;
Servo servoMotor;
char inChar;
String string="";
int vel = 1500;

//Configuracion de puerto serial y reservacion de variable string
void setup() {
  ESC.attach(9);//Asigno el pin 9 al motor
  ESC.writeMicroseconds(1500);//calibro en punto muerto
  servoMotor.attach(10);//Asigno el pin 10 al servomotor
  servoMotor.write(90);
  delay(5000); //Esperar 5 segundos para hacer la activacion
  Serial.begin(9600);
  string.reserve(200);
}

void loop(){
  if (Serial.available()){
//Lectura de caracteres   
   inChar = Serial.read();

   if (inChar==','){
    Serial.print("Aceleracion: ");
    Serial.println(string);
    cambiaAceleracion(string.toInt());
    string="";
   }
//Imprime la variable con los caracteres acumulados hasta la ","   
   else if (inChar=='|'){
    Serial.print("Direccion: ");
    Serial.println(string);
    cambiaDireccion(string.toInt());
//Borra la variable string para almacenar nuevos datos
    string=""; 
   }
   else{
    //Suma de caracteres en variable string
    string+=inChar;
   }
  }
  
}

bool cambiaAceleracion(int aceleracion){
  ESC.writeMicroseconds(vel+(5*aceleracion)); //Generar un pulso con el numero recibido
  return true;
}

void cambiaDireccion(int grados){
  servoMotor.write(grados);
}



