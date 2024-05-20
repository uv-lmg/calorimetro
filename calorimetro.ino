#include <OneWire.h>                 //Se importan las librerías
#include <DallasTemperature.h>

#define Pin 2                        //Se declara el pin donde se conectará la DATA
OneWire ourWire(Pin);                //Se establece el pin declarado como bus para la comunicación OneWire
DallasTemperature sensors(&ourWire); //Se llama a la librería DallasTemperature

static float tiempo; //Se declara el tiempo como float para su uso
static bool started = false; //Estado del programa, ya inicio?

void setup() {       
  sensors.begin();                    
  Serial.begin(9600);    //Se inician los sensores
}

void loop() {

  if (!started){ //Checa si el programa inició y si no, imprimir titulo de los datos
      Serial.print("\n Tiempo (s) |  Temperatura (°C) \n"); 
      started = true;
  }


  tiempo = millis();   //El tiempo es equivalente a los milisegundos transcurridos
  Serial.print((tiempo)/1000);    //Se dividen los milisegundos entre 1000. 
  Serial.print("  ");

  sensors.requestTemperatures();  //Prepara el sensor para la lectura
  Serial.print(sensors.getTempCByIndex(0));  //Se lee e imprime la temperatura en grados Centigrados

  Serial.print(" \n");
  delay(1000);  //Se provoca una parada de 1 segundo antes de la próxima lectura
 
}