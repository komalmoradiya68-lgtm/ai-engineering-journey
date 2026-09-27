#include <iostream>

int main() {
    std::cout << "========================================" << std::endl;
    std::cout << "      PROJECT MIT // ROBOT CONTROLLER   " << std::endl;
    std::cout << "========================================" << std::endl;

    // Sensor inputs
    double battery_voltage = 11.2;  // Volts (healthy range: 10.5V - 12.6V)
    double distance_cm = 12.5;       // Ultrasonic sensor reading (distance to obstacle)

    std::cout << "Telemetry: Battery = " << battery_voltage << "V | Distance = " << distance_cm << "cm\n\n";

    // Autonomous Decision Logic:
    if (battery_voltage < 10.0) {
        std::cout << "[STATUS] CRITICAL: Low battery! Shutting down systems." << std::endl;
    } 
    else if (distance_cm <= 15.0) {
        std::cout << "[STATUS] OBSTACLE DETECTED (" << distance_cm << "cm)! Emergency brake engaged." << std::endl;
    } 
    else {
        std::cout << "[STATUS] Path is clear. Motors running forward at full speed." << std::endl;
    }

    return 0;
}
