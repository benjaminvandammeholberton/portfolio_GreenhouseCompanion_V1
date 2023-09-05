#include <HTTPClient.h>
#include <WiFi.h>
#include <ArduinoJson.h> // Include the ArduinoJson library

const char *ssid = "";        // replace with wifi id
const char *password = "";    // Replace with wifi password
const char *serverUrl = "";   // Replace with your server's URL
const int analogInPin32 = 32; // GPIO pin 32 sensor1
const int analogInPin33 = 33; // GPIO pin 33 sensor2
const int analogInPin35 = 35; // GPIO pin 35 sensor3
const int relayPin = 26;

void setup()
{
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    // Initialize the GPIO pin as an output
    pinMode(relayPin, OUTPUT);
    digitalWrite(26, HIGH);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
}

void loop()
{
    digitalWrite(26, HIGH); // Turn on the relay
    // Read the analog value from the photoresistor
    int sensorValue1 = analogRead(analogInPin32);
    int sensorValue2 = analogRead(analogInPin33);
    int sensorValue3 = analogRead(analogInPin35);

    // Create a JSON document
    StaticJsonDocument<200> jsonDocument;
    jsonDocument["sensor_1"] = sensorValue1;
    jsonDocument["sensor_2"] = sensorValue2;
    jsonDocument["sensor_3"] = sensorValue3;

    // Serialize the JSON document to a string
    String jsonString;
    serializeJson(jsonDocument, jsonString);

    // Create an HTTPClient object
    HTTPClient http;

    // Send the POST request with the JSON payload to the Flask server
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");
    int httpCode = http.POST(jsonString);

    if (httpCode > 0)
    {
        String response = http.getString();
        Serial.println(response);

        // Parse the JSON response
        DynamicJsonDocument jsonDoc(200);
        DeserializationError error = deserializeJson(jsonDoc, response);

        // Check for parsing errors
        if (!error)
        {
            // Check if the response contains "true"
            bool relayState = jsonDoc["relay"];
            if (relayState)
            {
                // Turn on the relay module (assuming GPIO pin 26 is used)
                digitalWrite(relayPin, LOW); // Turn on the relay
                Serial.println("Relay turned on");
                delay(5000);
                digitalWrite(relayPin, HIGH);
                Serial.println("Relay turned off");
            }
        }
        else
        {
            Serial.println("Error parsing JSON");
        }

        // Separate else block for handling HTTP request error
        if (httpCode <= 0)
        {
            Serial.println("Error on HTTP request");
        }

        http.end();

        delay(60000); // Delay between readings
    }
}
