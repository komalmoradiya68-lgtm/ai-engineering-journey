/*
 * SHLOK // ROBOTICS & EMBEDDED SYSTEM 01
 * Target Board: Arduino UNO (ATmega328P)
 * FQBN: arduino:avr:uno
 * Architecture: Non-blocking state machine with telemetry
 */

#include <Arduino.h>

// Hardware Pin Definitions
constexpr uint8_t LED_HEARTBEAT_PIN = 13; // Built-in LED on ATmega328P (Port B, Bit 5)

// Timing configurations (Non-blocking loop pattern)
constexpr unsigned long HEARTBEAT_INTERVAL_MS = 500;
unsigned long previousMillis = 0;
bool ledState = false;
uint32_t cycleCounter = 0;

void setup() {
    // 1. Initialize Serial Telemetry Port at 115200 baud
    Serial.begin(115200);
    while (!Serial && millis() < 2000) {
        // Wait up to 2 seconds for USB serial port connection
    }

    // 2. Configure Hardware Pins
    pinMode(LED_HEARTBEAT_PIN, OUTPUT);

    // 3. Telemetry Boot Announcement
    Serial.println(F("==========================================="));
    Serial.println(F("[SYSTEM]: ARDUINO UNO ROBOTICS CORE ONLINE"));
    Serial.println(F("[TOOLCHAIN]: ARDUINO-CLI + VS CODE OK"));
    Serial.println(F("[ARCH]: ATmega328P @ 16 MHz"));
    Serial.println(F("==========================================="));
}

void loop() {
    unsigned long currentMillis = millis();

    // Non-blocking Heartbeat Timer
    if (currentMillis - previousMillis >= HEARTBEAT_INTERVAL_MS) {
        previousMillis = currentMillis;
        ledState = !ledState;
        digitalWrite(LED_HEARTBEAT_PIN, ledState ? HIGH : LOW);
        cycleCounter++;

        // Periodic telemetry packet
        Serial.print(F("[TELEMETRY] T: "));
        Serial.print(currentMillis);
        Serial.print(F(" ms | Cycle: "));
        Serial.print(cycleCounter);
        Serial.print(F(" | Heartbeat: "));
        Serial.println(ledState ? F("HIGH") : F("LOW"));
    }
}
