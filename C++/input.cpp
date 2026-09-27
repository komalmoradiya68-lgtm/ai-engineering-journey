#include <iostream>
int main()
{
    double mass;
    double velocity;
    std::cout << "Enter vehicle mass in kg:" << std::endl;
    std::cin >> mass;
    std::cout << "Enter vehicle velocity in m/s:" << std::endl;
    std::cin >> velocity;
    double kinetic_energy = 0.5 * mass * velocity * velocity;
    std::cout << "Vehicle Kinetic Energy: " << kinetic_energy << " Joules" << std::endl;
    return 0;
}
