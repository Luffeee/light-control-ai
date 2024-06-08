#include <string>
#include "WiFi.h"
#include "WebSocketsClient.h"

#define LED 15

const char *ssid = "Spider paul";
const char *password = "7500@@85";

WebSocketsClient webSocket;

void WebSocketEvent(WStype_t type, uint8_t *payload, size_t length);
void processMessage(uint8_t *payload);

void connectToWiFi() {
  Serial.print("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
}

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  connectToWiFi();
  webSocket.begin("192.168.0.104", 8000, "/ws/esp32");
  webSocket.onEvent(WebSocketEvent);
  webSocket.setReconnectInterval(5000);
}

void loop() {
  webSocket.loop();
}

void WebSocketEvent(WStype_t type, uint8_t *payload, size_t length) {
  switch (type) {
    case WStype_DISCONNECTED:
      Serial.printf("WebSocket disconnected\n");
      break;
    case WStype_CONNECTED:
      Serial.printf("WebSocket connected\n");
      break;
    case WStype_TEXT:
      Serial.printf("Received: %s\n", payload);
      processMessage(payload);
      break;
    case WStype_ERROR:
      Serial.printf("WebSocket error\n");
      break;
  }
}

void processMessage(uint8_t *payload) {
  if (strcmp((char*) payload, "LedState: on") == 0) {
    digitalWrite(LED, HIGH);
  }
  if (strcmp((char*) payload, "LedState: off") == 0) {
    digitalWrite(LED, LOW);
  }
}