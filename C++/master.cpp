// PROJECT 1: Drone Powertrain & Battery Sentinel

#include <iostream>

int main()
{
    double voltage;
    double current;
    std::cout << "ENTER YOUR VOLTAGE(in Volts)" << std::endl;
    std::cin >> voltage;
    std::cout << "ENTER YOUR CURRENT(in Amperes)" << std::endl;
    std::cin >> current;
    double power = voltage * current;
    std::cout << "[POWER TELEMETRY] " << power << " Watts dissipated" << std::endl;
    if (voltage < 10.5 || power > 300.0)
    {
        std::cout << "⟹ [CRITICAL ABORT] High thermal overload or low cell voltage! Immediate emergency landing!" << std::endl;
    }
    else if (power >= 150.0 && power <= 300.0)
    {
        std::cout << " [MAX THRUST] Heavy climb or high wind resistance. ESC cooling fan 100%." << std::endl;
    }
    else if (power < 150.0 && voltage >= 10.5)
    {
        std::cout << " [CRUISE NOMINAL] Powertrain operating within safe efficiency curve." << std::endl;
    }
    // 🛰️ PROJECT 2: Rocket Propellant Burn & Altitude Simulator
    double fuel_mass;
    std::cout << "Enter Initial Propellant Mass (kg):" << std::endl;
    std::cin >> fuel_mass;
    int second = 0;
    double altitude = 0.0;
    while (fuel_mass > 0.0)
    {
        second = second + 1;
        fuel_mass = fuel_mass - 25.0;
        altitude = altitude + 80.0;
        std::cout << "=== MAIN ENGINE IGNITION ===" << std::endl;
        std::cout << "Fuel Remaining: " << fuel_mass << "Altitude: " << altitude << std::endl;
    }
    if (altitude >= 300.0)
    {
        std::cout << "[MECO] Main Engine Cutoff. Propellant fully depleted." << std::endl;
        std::cout << "[SUB-ORBITAL INSERTION] Target altitude achieved. Deploying payload." << std::endl;
    }
    else
    {
        std::cout << "[MISSION FAILURE] Insufficient fuel to clear lower atmosphere." << std::endl;
    }
    // 🤖 PROJECT 3: Mars Rover 4-Directional LiDAR Collision Scanner
    double lidar_distances[4] = {0.85, 3.40, 5.10, 1.10};
    double distance_sum = 0.0;
    std::cout << "=== COMMENCING 360-DEGREE LIDAR SWEEP ===" << std::endl;
    for (int i = 0; i < 4; i++)
    {
        distance_sum = distance_sum + lidar_distances[i];
        if (lidar_distances[i] < 1.5)
        {
            std::cout << " [COLLISION HAZARD] Sensor [ " << i << " ]:" << lidar_distances[i] << " m! Obstacle dangerously close!" << std::endl;
        }
        else
        {
            std::cout << "[CLEAR] Sensor [ " << i << "]: " << lidar_distances[i] << " m | Path unobstructed." << std::endl;
        }
    }
    double average_distance = distance_sum / 4.0;
    std::cout << "=== SWEEP COMPLETE ===" << std::endl;
    std::cout << "Average Environmental Clearance:" << average_distance << " meters." << std::endl;
    return 0;
}
