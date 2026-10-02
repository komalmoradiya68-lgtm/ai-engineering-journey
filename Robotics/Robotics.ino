/*
 * SHLOK // ROBOTICS & EMBEDDED SYSTEM 03
 * Circuit 03: The 4-Stage Tactical Dimmer (PWM + Edge-Triggered State Machine)
 * Hardware:
 *   - Pin ~11 (PWM Output): LED Anode via 220Ω Resistor
 *   - Pin 2   (Digital Input): Tactile Push Button (INPUT_PULLUP)
 *   - GND:    Common Ground Rail
 */

#include <Arduino.h>

// Hardware Pin Definitions
constexpr uint8_t PIN_LED_PWM  = 11; // Must be a '~' PWM pin (3, 5, 6, 9, 10, 11)
constexpr uint8_t PIN_BUTTON   = 2;  // Hardware interrupt/digital pin with internal pullup

// 4-Stage Power Levels (8-bit PWM: 0 to 255)
constexpr uint8_t POWER_LEVELS[4] = {0, 35, 110, 255};
const char* const MODE_NAMES[4]   = {"STANDBY (OFF)", "STEALTH (14%)", "CRUISE (43%)", "MAX BLAST (100%)"};

// State Machine Variables
uint8_t currentMode = 0;              // Starts at 0 (OFF)
int lastButtonState = HIGH;           // Previous stable reading
int previousReading = HIGH;           // Raw reading for debouncing
unsigned long lastDebounceTime = 0;
constexpr unsigned long DEBOUNCE_DELAY_MS = 40; // 40ms mechanical filter

void setup() {
    Serial.begin(115200);
    while (!Serial && millis() < 1500) {
        // Wait briefly for serial monitor connection
    }

    pinMode(PIN_LED_PWM, OUTPUT);
    pinMode(PIN_BUTTON, INPUT_PULLUP);

    // Initialize to Mode 0 (OFF)
    analogWrite(PIN_LED_PWM, POWER_LEVELS[currentMode]);

    Serial.println(F("==========================================="));
    Serial.println(F("[SYSTEM]: CIRCUIT 03 TACTICAL DIMMER ARMED"));
    Serial.println(F("[ARCH]  : 8-BIT HARDWARE PWM (Timer2 @ 490Hz)"));
    Serial.println(F("[INPUT] : PIN 2 EDGE-TRIGGERED STATE MACHINE"));
    Serial.println(F("==========================================="));
    Serial.print(F("[BOOT] Mode 0: "));
    Serial.println(MODE_NAMES[currentMode]);
}

void loop() {
    unsigned long currentMillis = millis();
    int rawReading = digitalRead(PIN_BUTTON);

    // 1. Debounce Filter: Reset timer if switch bounced
    if (rawReading != previousReading) {
        lastDebounceTime = currentMillis;
    }

    // 2. Edge Detection: Process state change only after signal stabilizes
    if ((currentMillis - lastDebounceTime) > DEBOUNCE_DELAY_MS) {
        if (rawReading != lastButtonState) {
            lastButtonState = rawReading;

            // FALLING EDGE: Button was just clicked down (HIGH -> LOW)
            if (lastButtonState == LOW) {
                // Cycle through 0 -> 1 -> 2 -> 3 -> 0 using modulo arithmetic
                currentMode = (currentMode + 1) % 4;

                // Apply Hardware PWM Duty Cycle to Silicon
                analogWrite(PIN_LED_PWM, POWER_LEVELS[currentMode]);

                // Telemetry Broadcast
                Serial.print(F("[CLICK EVENT] ──► Mode "));
                Serial.print(currentMode);
                Serial.print(F(": "));
                Serial.print(MODE_NAMES[currentMode]);
                Serial.print(F(" | PWM: "));
                Serial.print(POWER_LEVELS[currentMode]);
                Serial.println(F(" / 255"));
            }
        }
    }

    previousReading = rawReading;
}
