#include <ArduinoJson.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>

// Sensor Definitions
#define ONE_WIRE_BUS 4  
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

#define DHT_DO_PIN 26 // Define the single DO pin for the DHT22
#define DHTTYPE DHT22  // Specify the sensor type
DHT dht(DHT_DO_PIN, DHTTYPE);

// WiFi Credentials
const char* ssid = "GalaxyA15";
const char* password = "Sandile123";
const char* serverUrl = "http://192.168.107.11:5000/update"; // Replace with actual server IP

WiFiClient client;
HTTPClient http;

// Define digital output (DO) pins
#define Infra_red 14
#define LDR 34  // analog pin

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected! IP Address: ");
  Serial.println(WiFi.localIP());

  sensors.begin();
  dht.begin();

  pinMode(DHT_DO_PIN, INPUT);  // Set the DHT22 pin as input
  pinMode(Infra_red , INPUT);
  pinMode(LDR, INPUT);  // LDR sensor pin
}

void loop() {
  sensors.requestTemperatures();
  float ds18b20Temp = sensors.getTempCByIndex(0);  // Get DS18B20 temperature
  float dhtTemp = dht.readTemperature(); // Get DHT22 temperature
  float dhtHumidity = dht.readHumidity(); // Get DHT22 humidity

  bool irDetected = digitalRead(Infra_red);  
  int ldrValue1 = analogRead(LDR);  // LDR sensor light intensity value (analog)

  // Debugging Prints
  Serial.println("DS18B20 Temperature: " + String(ds18b20Temp));
  Serial.println("DHT22 Temperature: " + String(dhtTemp));
  Serial.println("DHT22 Humidity: " + String(dhtHumidity));
  Serial.println("LDR: " + String(ldrValue1));  
  Serial.println("Infrared Sensor: " + String(irDetected));

  StaticJsonDocument<200> jsonData;
  jsonData["DS18B20_Temperature"] = ds18b20Temp;
  jsonData["DHT22_Temperature"] = dhtTemp; 
  jsonData["DHT22_Humidity"] = dhtHumidity;
  jsonData["LDR"] = ldrValue1;  
  jsonData["InfraRed"] = irDetected;

  String jsonOutput;
  serializeJson(jsonData, jsonOutput);
  
  http.begin(client, serverUrl);
  http.addHeader("Content-Type", "application/json");

  Serial.println("Sending JSON Data...");
  Serial.println(jsonOutput);

  int httpResponseCode = http.POST(jsonOutput);
  Serial.println("Server Response Code: " + String(httpResponseCode));

  if (httpResponseCode > 0) {
    Serial.println("Server Response: " + http.getString());
  } else {
    Serial.println("Error Sending Request!");
  }

  http.end();
  delay(5000);
}