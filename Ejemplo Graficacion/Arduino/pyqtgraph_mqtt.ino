#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ARDUINO_UNOWIFIR4)
  #include <WiFiS3.h>
#endif
#include <PubSubClient.h>

const char* ssid = "InstVirtual";                    // NOTA: cambiar este parametro antes de grabar el programa en el ESP32
const char* password = "37418601";                          // NOTA: cambiar este parametro antes de grabar el programa en el ESP32

const char* mqtt_server = "192.168.0.100";             // servidor MQTT

const char* ID = "AESP32_1";

uint16_t valorAdc1, valorAdc2;
String command;
uint8_t flagDato = 0;
char msg[20];

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
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

void reconnect(){
  while(!client.connected()){                           // mientras el cliente esta desconectado del servidor, intentamos una reconexion
    Serial.print("\nReconectando servidor MQTT...");   
    if(client.connect(ID)){                             // si el cliente ya se conecto al servidor
      Serial.println("conectado");
      client.subscribe("iv/adc1/cmd");                    // no suscribimos al topico que desamos (esto no es obligatorio si solo se va a publicar)
      client.subscribe("iv/adc2/cmd");
    }else{
      Serial.print("Fallo, rc = ");                     // si hay alguna falla en la conexion
      Serial.print(client.state());                     // desplegamos el error de conexion
      Serial.println("Reintentando en 5 segundo...");   // reintentamos una reconexion en 5 segundos
      delay(5000);
    }
  }
}

void callback(char* topic, byte* message, unsigned int length){
  String msgTemp;

  for(int i = 0; i < length; i++){                      // convertimos todo los datos del mensaje de byte a char y lo concatenamos en msgTemp
    msgTemp += (char)message[i];
  }

  if(String(topic) == "iv/adc1/cmd"){
    command = msgTemp;
    flagDato = 1;
    Serial.println(command);
  }

  if(String(topic) == "iv/adc2/cmd"){
    command = msgTemp;
    flagDato = 1;
    Serial.println(command);
  }
}

void loop() {
  if(!client.connected()){                              // checamos si el cliente esta conectado al servidor
    reconnect();                                        // si no esta conectado reconectamos el cliente al servidor
  }
  
  if(flagDato){
    flagDato = 0;
    if(command == "A"){
      valorAdc1 = analogRead(A0);
      Serial.println(valorAdc1);
      sprintf(msg, "%lu\n", valorAdc1);
      client.publish("iv/adc1/val", msg);
    }else if(command == "B"){
      valorAdc2 = analogRead(A1);
      Serial.println(valorAdc2);
      sprintf(msg, "%lu\n", valorAdc2);
      client.publish("iv/adc2/val", msg);
    }
  }
  client.loop();
}
