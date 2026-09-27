#include <iostream>
#include <string>

// 1. REUSABLE FUNCTION: Calculate battery consumption
double compute_remaining_battery(double current_battery, double flight_minutes, double drain_rate_per_min) {
    double drained = flight_minutes * drain_rate_per_min;
    double remaining = current_battery - drained;
    if (remaining < 0.0) {
        remaining = 0.0;
    }
    return remaining;
}

// 2. REUSABLE VOID FUNCTION: Print Mission Header
void print_drone_banner(std::string name, int mission_id) {
    std::cout << "==========================================" << std::endl;
    std::cout << "   MISSION CONTROL // DRONE: " << name << std::endl;
    std::cout << "   MISSION ID: #" << mission_id << std::endl;
    std::cout << "==========================================" << std::endl;
}

int main() {
    // 3. VARIABLES & STRINGS
    std::string drone_callsign = "Falcon-X";
    int mission_number = 101;
    double battery = 100.0;          // Percent
    double drain_rate = 3.5;         // Drains 3.5% per minute
    
    print_drone_banner(drone_callsign, mission_number);

    // 4. USER INTERACTION (std::cin & std::cout)
    std::cout << "\nEnter planned flight duration in minutes: ";
    double flight_time = 15.0; // Simulated input: 15 minutes
    std::cout << flight_time << " min (automated simulation input)\n";

    // 5. CALLING OUR FUNCTION
    battery = compute_remaining_battery(battery, flight_time, drain_rate);
    std::cout << "Battery remaining after flight: " << battery << "%\n\n";

    // 6. SWITCH-CASE: Select Flight Mode
    char mode = 'A'; // 'A' = Autonomous, 'M' = Manual, 'R' = Return to Home
    std::cout << "Flight Mode Status: ";
    switch (mode) {
        case 'A':
            std::cout << "AUTONOMOUS NAVIGATION [ON]" << std::endl;
            break;
        case 'M':
            std::cout << "MANUAL PILOT OVERRIDE" << std::endl;
            break;
        case 'R':
            std::cout << "RETURN-TO-HOME ACTIVATED" << std::endl;
            break;
        default:
            std::cout << "UNKNOWN FLIGHT MODE" << std::endl;
            break;
    }

    // 7. ARRAYS & FOR-LOOP: Telemetry Altitude Log (meters)
    double altitude_log[5] = {10.5, 25.0, 48.2, 50.0, 30.1};
    std::cout << "\nScanning Altitude Sensor Log (5 Waypoints):" << std::endl;

    double max_altitude = 0.0;
    for (int i = 0; i < 5; i++) {
        std::cout << "  Waypoint " << (i + 1) << ": " << altitude_log[i] << " meters" << std::endl;
        
        // IF-CONDITION inside loop: Find peak altitude
        if (altitude_log[i] > max_altitude) {
            max_altitude = altitude_log[i];
        }
    }

    std::cout << "\nPeak Altitude Reached: " << max_altitude << " meters" << std::endl;
    
    // 8. FINAL SAFETY CHECK
    if (battery < 20.0) {
        std::cout << "[WARNING] Low battery landing sequence initiated!" << std::endl;
    } else {
        std::cout << "[STATUS] Drone landed safely. Systems nominal." << std::endl;
    }

    return 0;
}
