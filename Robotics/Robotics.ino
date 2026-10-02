#include <Arduino.h>

// Pins
constexpr uint8_t PIN_LED_12 = 12;
constexpr uint8_t PIN_LED_13 = 13; // Built-in & backup
constexpr uint8_t PIN_BUTTON = 2;

void setup() {
    Serial.begin(115200);
    pinMode(PIN_LED_12, OUTPUT);
    pinMode(PIN_LED_13, OUTPUT);
    pinMode(PIN_BUTTON, INPUT_PULLUP); // 30k internal pull-up

    Serial.println(F("[SYSTEM]: BUTTON CONTROLLER ARMED"));
}

void loop() {
    int buttonState = digitalRead(PIN_BUTTON);

    // Instantaneous, zero-lag button response:
    if (buttonState == LOW) {
        // BUTTON PRESSED -> Turn BOTH Pin 12 and Pin 13 ON!
        digitalWrite(PIN_LED_12, HIGH);
        digitalWrite(PIN_LED_13, HIGH);
    } else {
        // BUTTON RELEASED -> Turn OFF!
        digitalWrite(PIN_LED_12, LOW);
        digitalWrite(PIN_LED_13, LOW);
    }
}
