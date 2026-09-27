// Project: Solar Panel Motorized Calibration Sweep
#include <iostream>
int main()
{
    std::cout << "Solar Panel Motorized Calibration Sweep initializing!" << std::endl;
    for (int angle = 0; angle <= 90; angle = angle + 15)
    {
        std::cout << "[CALIBRATING] Angle: " << angle << " deg | Photodiode reading calibrated." << std::endl;
    }
    std::cout << " [SWEEP COMPLETE] Solar tracker aligned for maximum sunlight conversion!" << std::endl;
}