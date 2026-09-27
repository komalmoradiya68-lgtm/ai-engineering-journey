// Project: Hydraulic Pressure Relief Valve
#include <iostream>
int main()
{
    double pressure_psi;
    std::cout << "Enter your pressure_psi" << std::endl;
    std::cin >> pressure_psi;
    if (pressure_psi > 150.0)
    {
        std::cout << " [EMERGENCY] Maximum pressure exceeded! Opening hydraulic relief valve!" << std::endl;
    }
    else
    {
        std::cout << "[SYSTEM NORMAL] Pressure within safe structural tolerance." << std::endl;
    }
    return 0;
}