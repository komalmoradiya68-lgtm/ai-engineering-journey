# ⚡ EMBEDDED ROBOTICS & HARDWARE PROTOTYPING PROTOCOL

When guiding, designing, or debugging physical circuits, breadboard layouts, and embedded C++ for Arduino/ATmega328P:

### 1. Default to Silicon Pull-Ups (`INPUT_PULLUP`)
- **Rule:** Never instruct or recommend external pull-down resistors with extra +5V wiring for digital switches.
- **Implementation:** Always configure digital input pins with `pinMode(pin, INPUT_PULLUP)` using active-low logic:
  - `LOW` (0V) = Switch Closed / Pressed
  - `HIGH` (5V) = Switch Open / Released
- **Rationale:** Reduces physical button wiring to exactly TWO wires (Pin to Button, Button to GND), eliminates resistor mismatch bugs (e.g. 220Ω vs 10kΩ), and uses the microcontroller's internal 30kΩ FET resistor.

### 2. The MB-102 Split Power Rail Invariant
- **Rule:** Always account for the physical break/split in full-size (830-point) breadboard power rails at Row 30.
- **Implementation:** When routing Ground across distant sections of the breadboard, instruct connecting directly to one of the Arduino's three `GND` pins or physically bridging the top and bottom rails with a dedicated jumper. Never assume the long blue line is continuous end-to-end without verification.

### 3. The 3-Step Physical Isolation Diagnostic Protocol
When a physical circuit fails or produces ambiguous symptoms, execute this diagnostic sequence before changing code:
- **Step A (Actuator / LED Health Check):** Move the signal wire directly to the Arduino `5V` pin. If the LED does not glow, diagnose P-N junction polarity (flip legs) or ground return path.
- **Step B (Input / Logic Verification via Bare Wire):** Unplug the switch wire and touch its bare metal pin directly to an Arduino `GND` pin. If the serial monitor logs the event or the LED responds, the C++ code and GPIO pin are 100% verified; the defect is strictly mechanical switch alignment.
- **Step C (Switch Metrology):** Use the multimeter's continuity buzzer mode to probe and verify which two switch legs actually close upon mechanical depression before inserting into the breadboard.

### 4. Support Student Netlist Autonomy
- **Rule:** Do not force students to follow rigid third-party row numbers from online tutorials.
- **Implementation:** Support the student's preferred row choices (e.g., Rows 20, 22, 25, 34, 35) while verifying the electrical netlist (common ground, node isolation, and correct resistor current limiting: $I = (V_{supply} - V_f) / R$).
