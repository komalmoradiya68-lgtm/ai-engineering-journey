#include <iostream>
#include <bitset> // Allows us to print numbers in 8-bit binary format
#include <thread> // Used for sleeping/pausing on a PC
#include <chrono> // Used for time (milliseconds)

int main()
{
    // Simulate an 8-bit hardware register (all 8 switches start OFF)
    uint8_t simulated_PORTB = 0b00000000;

    std::cout << "=== BARE-METAL REGISTER SIMULATION (PC) ===" << std::endl;
    std::cout << "Starting PORTB: " << std::bitset<8>(simulated_PORTB) << " (All pins OFF)\n\n";

    for (int cycle = 1; cycle <= 6; cycle++)
    {
        // Toggle Bit 5 (Pin 13) using the XOR operator (^)
        simulated_PORTB ^= (1 << 5);

        // Check if Bit 5 is 1 (ON) or 0 (OFF) using the AND operator (&)
        bool led_state = simulated_PORTB & (1 << 5);

        std::cout << "Cycle " << cycle << " | PORTB: "
                  << std::bitset<8>(simulated_PORTB)
                  << " -> Pin 13 is " << (led_state ? "[ON] (5V)" : "[OFF] (0V)")
                  << std::endl;

        // Pause for 500 milliseconds (like delay(500) on Arduino)
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }

    std::cout << "\nSimulation Complete. You just controlled an 8-bit register!\n";
    return 0;
}