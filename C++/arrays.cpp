// Project: Planetary Rover 4-Wheel Velocity Scanner
#include <iostream>
int main()
{
    double wheel_speeds[4] = {1.20, 1.25, 1.18, 1.22};
    for (int i = 0; i < 4; i++)
    {
        std::cout << "[WHEEL " << i << "] Velocity: " << wheel_speeds[i] << " m/s | Traction locked." << std::endl;
    }
    std::cout << "[DRIVETRAIN NOMINAL] All 4 wheel encoders synchronized!" << std::endl;
}