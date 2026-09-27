// Lunar rover over moon!
#include <iostream>
int main()
{
    int speed = 4;
    int time = 30;
    int energy_rate = 5;
    int distance = speed * time;
    int Total_Energy = distance * energy_rate;
    std::cout << "Total distance covered: " << distance << " meters" << std::endl;
    std::cout << "Total energy consumed: " << Total_Energy << " Joules" << std::endl;
    double g = 9.8;
    double v = 11.1;
    double o = 2.5;
    double i = v / o;
    double p = v * i;
    std::cout << "Motor Current: " << i << " Amperes" << std::endl;
    std::cout << "Power Dissipated: " << p << " Watts" << std::endl;
    return 0;
}