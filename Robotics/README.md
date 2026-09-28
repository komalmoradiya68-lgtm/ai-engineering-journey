# 🤖 SHLOK // ROBOTICS & ARDUINO EMBEDDED WORKSPACE

Welcome to your official Arduino development environment configured in Visual Studio Code. This workspace bridges high-level C++ with bare-metal microcontroller registers and physical circuit dynamics.

---

## 🛠️ 1. Installed Core Tools & Extensions

| Tool / Component | Version / Identifier | Purpose |
|---|---|---|
| **Arduino CLI** | `v1.5.1` (Official Arduino SA) | Core compiler engine, board package manager, and uploader. Added to system & user PATH. |
| **Arduino AVR Platform** | `v1.8.8` | Official AVR toolchain (`avr-gcc 7.3.0`, `avrdude 8.0.0`, `Arduino.h` core headers). |
| **Arduino Community Extension** | `vscode-arduino.vscode-arduino-community` | Primary VS Code interface for board selection, library management, and sketch verification. |
| **Microsoft Serial Monitor** | `ms-vscode.vscode-serial-monitor` | High-speed, official integrated serial communication terminal. |
| **Wokwi Simulator** | `wokwi.wokwi-vscode` | Microcontroller and circuit simulator inside VS Code (no physical board required). |
| **C/C++ IntelliSense** | `ms-vscode.cpptools` | Configured with AVR core paths, eliminating red squiggles for Arduino functions and registers. |

---

## 🚀 2. Quick Execution Guide

### A. Compile Active Sketch
* **Keystroke Shortcut:** Press **`Ctrl + Shift + B`** (triggers the default build task).
* **CLI Alternative:**
  ```powershell
  arduino-cli compile --fqbn arduino:avr:uno Robotics.ino
  ```

### B. Upload to Physical Board
1. Plug your Arduino Uno / Nano into any USB port.
2. Check your COM port in the terminal:
   ```powershell
   arduino-cli board list
   ```
3. Upload via VS Code: Press `Ctrl + Shift + P` $\rightarrow$ `Tasks: Run Task` $\rightarrow$ `Arduino: Upload Sketch (Auto/COM3)`
   *(Or modify `"port"` in `.vscode/arduino.json` to match your COM port).*

### C. Open the Serial Monitor
* Click the **Serial Monitor** tab in the bottom panel of VS Code (next to Terminal / Output).
* Set Port to your active Arduino COM port.
* Set Baud Rate to **`115200`** (matching `Serial.begin(115200)` in [Robotics.ino](file:///f:/DEV/Shlok-2/me/Robotics/Robotics.ino)).
* Click **Start Monitoring**.

### D. Run Circuit Simulation in Wokwi (Virtual Hardware)
* Ensure you have compiled the sketch at least once (`Ctrl + Shift + B`) to generate the `.hex` file.
* Press **`Ctrl + Shift + P`** $\rightarrow$ Type **`Wokwi: Start Simulator`** $\rightarrow$ Press Enter.
* Alternatively, right-click [diagram.json](file:///f:/DEV/Shlok-2/me/Robotics/diagram.json) and select **Open Wokwi Simulator**.
* An interactive virtual Arduino Uno with an animated LED and virtual Serial output will run directly inside your editor.

---

## 📂 3. Workspace Configuration Architecture

```
Robotics/
├── .vscode/
│   ├── arduino.json            # Target board (arduino:avr:uno), port, build output
│   ├── c_cpp_properties.json   # C++ IntelliSense paths to Arduino15 core & avr-gcc
│   ├── settings.json           # Extension bindings to arduino-cli.exe
│   └── tasks.json              # Ctrl+Shift+B compile, upload, and board list tasks
├── build/                      # Compiled binaries (.hex, .elf) ready for Wokwi & avrdude
├── diagram.json                # Wokwi virtual breadboard / board layout
├── wokwi.toml                  # Wokwi firmware mapping file
├── Robotics.ino                # Non-blocking telemetry & heartbeat starter sketch
└── README.md                   # This operations manual
```

---

## 📖 4. Foundational Blueprints & Hardware Theory

* **Circuit Physics, LEDs & Power Architecture:** [CIRCUIT_PHYSICS_AND_POWER_GUIDE.md](file:///F:/DEV/Shlok-2/me/Engineering/Robotics/CIRCUIT_PHYSICS_AND_POWER_GUIDE.md)
* **Embedded Blueprint & Hardware Theory:** [CPP_EMBEDDED_ROBOTICS_BLUEPRINT.md](file:///F:/DEV/Shlok-2/me/Engineering/Python/mds/CPP_EMBEDDED_ROBOTICS_BLUEPRINT.md)
