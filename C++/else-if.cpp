// Project: Supersonic Wind Tunnel Mach Number Classifier
#include <iostream>
int main()
{
    double mach_number;
    std::cout << "Enter your mach number!" << std::endl;
    std::cin >> mach_number;
    if (mach_number < 0.8)
    {
        std::cout << "[SUBSONIC] Smooth laminar airflow. Normal flight." << std::endl;
    }
    else if (mach_number >= 0.8 && mach_number <= 1.2)
    {
        std::cout << "[TRANSONIC] Severe shockwave buffet zone! Aerodynamic trim active." << std::endl;
    }
    else if (mach_number > 1.2 && mach_number < 5.0)
    {
        std::cout << "[SUPERSONIC] Oblique shockwaves formed. Aerodynamic heating active." << std::endl;
    }
    else if (mach_number >= 5.0)
    {
        std::cout << "[HYPERSONIC] Thermal ionization of air! Heat shield cooling active." << std::endl;
    }
}