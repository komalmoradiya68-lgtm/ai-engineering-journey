/*
 * SHLOK // HARDWARE CALIBRATION & DIAGNOSTIC ENGINE
 * Pure solid-state visual test:
 * - Button NOT Pressed (HIGH): BLUE ON, RED OFF
 * - Button PRESSED (LOW):     BLUE OFF, RED ON
 */

#include <Arduino.h>

constexpr uint8_t PIN_LED_BLUE    = 13;
constexpr uint8_t PIN_LED_RED     = 12;
constexpr uint8_t PIN_BTN_TRIGGER = 2;

void setup() {
    Serial.begin(115200);
    pinMode(PIN_LED_BLUE, OUTPUT);
    pinMode(PIN_LED_RED, OUTPUT);
    pinMode(PIN_BTN_TRIGGER, INPUT_PULLUP);
}

void loop() {
    int buttonState = digitalRead(PIN_BTN_TRIGGER);

    if (buttonState == LOW) {
        // --- BUTTON PRESSED ---
        digitalWrite(PIN_LED_BLUE, LOW);
        digitalWrite(PIN_LED_RED, HIGH);
    } else {
        // --- BUTTON RELEASED ---
        digitalWrite(PIN_LED_BLUE, HIGH);
        digitalWrite(PIN_LED_RED, LOW);
    }
}
