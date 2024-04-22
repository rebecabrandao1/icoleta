#include <WiFi.h>
#include <HTTPClient.h>
#include "HX711.h"

const char* ssid = "EASY_LAB";
const char* password = "_easy_lab_";

// Pinos do sensor HX711
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;


const char* token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3ZWlnaHQiOjkuMDgsInBvaW50X2lkIjoxLCJpYXQiOjE3MTA0OTc5Mjh9.EkeireB8pAYu7UYzCcZo11EaNt6rrlZlmfbxaXNTIZM";
String baseUrl = "https://icoleta.netlify.app/descarte/";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  
  Serial.println("Conectado ao WiFi");

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {
  if (scale.is_ready()) {
    long reading = scale.read();
  
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(baseUrl + token); 
      http.addHeader("Content-Type", "application/x-www-form-urlencoded");

      String httpRequestData = "peso=" + String(reading); 
      int httpResponseCode = http.POST(httpRequestData);
      
      if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.println(httpResponseCode);
        Serial.println(response);
      } else {
        Serial.print("Erro no envio: ");
        Serial.println(httpResponseCode);
      }
      http.end();
    } else {
      Serial.println("Erro na conexão WiFi");
    }
  } else {
    Serial.println("Sensor HX711 não está pronto");
  }
  
  delay(10000); 
}
