// Project: Deep-Sea Submersible Descent Telemetry
#include <iostream>
int main()
{
    double depth = 0.0;
    std::cout << "YOUR DEPTH IS " << depth << std::endl;
    while (depth < 100.0)
    {
        depth = depth + 20.0;
        std::cout << "[DIVING] Current Depth: " << depth << " meters | Hull integrity nominal." << std::endl;
    }
    std::cout << "[SEABED REACHED] Touchdown at 100 meters. Deploying ocean exploration rover!" << std::endl;
}