// Modificar su SSID y PASSWORD de su red antes de compilar y grabar al ESP32

#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ARDUINO_UNOWIFIR4)
  #include <WiFiS3.h>
#endif
#include <PubSubClient.h>

// asignacion de pines ESP32-S3
//#define ADC_CHANNEL   1
//#define BTN_CHANNEL   14
//#define LED_CHANNEL   20

// asignacion de pines ESP32-C3
#define ADC_CHANNEL   0
#define BTN_CHANNEL   2
#define LED_CHANNEL   3

const char* ssid = "EL_NOMBRE_DE_SU_RED";                   // NOTA: cambiar este parametro antes de grabar el programa en el ESP32
const char* password = "EL_PASSWORD_DE_SU_RED";             // NOTA: cambiar este parametro antes de grabar el programa en el ESP32

const char* mqtt_server = "test.mosquitto.org";             // servidor MQTT en la nube
//const char* mqtt_server = "192.168.0.102";                  // servidor MQTT local

long lastMsg = 0;
int conta = 0;
char msg[20];
int valPot = 0;

WiFiClient espClient;                                   // creamos un objeto de la clase WiFiClient
PubSubClient client(espClient);                         // creamos un objeto de la clase PubSubClient


void setup(){
  Serial.begin(115200);                                 // iniciamos la UART a 115200
  pinMode(BTN_CHANNEL, INPUT);                                   // GPIO17 como entrada
  pinMode(LED_CHANNEL, OUTPUT);                                  // GPIO26 como salida
  setup_wifi();                                         // iniciamos la conexion a la red WiFi
  client.setServer(mqtt_server, 1883);                  // conectamos el ESP32 al serviro MQTT por el puerto 1883
  client.setCallback(callback);                         // creamos una funcion callback para recibir los datos del servidor
}

void setup_wifi(){
  Serial.print("\nConectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);                           // iniciamos la conexion al router
  while(WiFi.status() != WL_CONNECTED){                 // si no se ha podido conectar intentamas una reconexion medio segundo despues
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());                       // imprimimos la IP que nos asigno el router
}

/* Esta funcion recibe los datos del servidor cuando un cliente publica informacion al topico. 
 *  topic: Es el topico al que se ha publicado
 *  message: Es el mensaje que el cliente publico
 *  length: Este es el tamaño del mensaje
*/
void callback(char* topic, byte* message, unsigned int length){
  String msgTemp;                                       // creamos un string donde vamos a guardar el mensaje
  
  for(int i = 0; i < length; i++){                      // convertimos todo los datos del mensaje de byte a char y lo concatenamos en msgTemp
    msgTemp += (char)message[i];
  }

  if(String(topic) == "utt/esp32/led"){                     // comprobamos el topico que nos interesa
    if(msgTemp == "ON")                                 // comprobamos el mensaje (payload) si es "ON"
      digitalWrite(LED_CHANNEL, HIGH);                           // y encedemos el led conectador a la patita 22
    else if(msgTemp == "OFF")                           // si el mensaje que llego es "OFF"
      digitalWrite(LED_CHANNEL, LOW);                            // apagamos el led en la patita 22
  }
}

/* Esta funcion es llamada cuando se cierra la conexion entre el cliente (publicador o suscriptor) y el servidor (broker)*/
void reconnect(){
  while(!client.connected()){                           // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");   
    if(client.connect("ESP32_2")){                        // si el cliente ya se conecto al servidor
      Serial.println("conectado");
      client.subscribe("utt/esp32/led");                    // no suscribimos al topico que desamos (esto no es obligatorio si solo se va a publicar)
    }else{
      Serial.print("Fallo, rc = ");                     // si hay alguna falla en la conexion
      Serial.print(client.state());                     // desplegamos el error de conexion
      Serial.println("Reintentando en 5 segundo...");   // reintentamos una reconexion en 5 segundos
      delay(5000);
    }
  }
}

void loop(){
  if(!client.connected()){                              // checamos si el cliente esta conectado al servidor
    reconnect();                                        // si no esta conectado reconectamos el cliente al servidor
  }
  
  long varNow = millis();
  if(varNow - lastMsg > 500){                           // esperamos 500 milisegundos
    lastMsg = varNow;
    valPot = analogRead(ADC_CHANNEL);                            // leemos el canal analogico 34
    sprintf(msg,"%d", valPot);
    client.publish("utt/esp32/adc", msg);                   // publicamos el valor del ADC al topico deseado
    //Serial.println(valPot);
    if(digitalRead(BTN_CHANNEL) == 1){                           // verificamos el estado de la entrada 17
      client.publish("utt/esp32/boton", "1");               // publicamos un "0" si se presiono el boton
    }else{
      client.publish("utt/esp32/boton", "0");               // o publicamos un "1" si el boton no esta presionado
    }
  }
  client.loop();                                        // si el cliente ya esta conectador verificamos los mensajes entrantes constantemente y mantenemos la conexion con el servidor
}
