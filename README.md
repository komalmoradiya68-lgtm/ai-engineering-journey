# 🚀 The 60-Day First-Principles AI & Systems Engineering Journey

[![Language](https://img.shields.io/badge/C%2B%2B-23-blue.svg?logo=c%2B%2B)](https://isocpp.org/)
[![Language](https://img.shields.io/badge/Python-3.13-yellow.svg?logo=python)](https://python.org/)
[![Toolchain](https://img.shields.io/badge/Arduino%20CLI-1.5.1-teal.svg?logo=arduino)](https://arduino.github.io/arduino-cli/)
[![Methodology](https://img.shields.io/badge/Pedagogy-First%20Principles-red.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **"Bits Directing Atoms."**  
> An open-source, daily, high-friction engineering curriculum designed to master low-level silicon memory, hardware registers, mathematical physics, and artificial intelligence from scratch—without tutorial hell or black-box libraries.

---

## 🏛️ The Engineering Philosophy

Modern programming education has fallen into the trap of **"vibe-coding"**—passively watching 30-hour video tutorials and copy-pasting frameworks without understanding memory layouts, CPU cycles, or circuit physics.

This repository codifies the **3-Stage Cognitive Learning Loop**:
1. **Stage 1: Syntax & Silicon Memory Model:** Understand the exact byte cost in RAM (Stack vs Heap) and what the CPU does under the hood.
2. **Stage 2: Reference Architecture:** Review working real-world systems (aerospace telemetry, robotics drivers).
3. **Stage 3: Novel Science Transfer:** Solve unfamiliar, un-copyable physical science problems (orbital mechanics, kinetic energy, nuclear safety, circuit laws).

---

## 📂 Repository Topology

```text
ai-engineering-journey/
│
├── C++/                                # Track A: Low-level systems & bare-metal compute
│   ├── session1.cpp ... arrays.cpp     # Lessons 01 - 10 (Syntax, Memory, Loops, Arrays)
│   ├── master.cpp                      # Capstone Sprint: 3-in-1 Master Aerospace Mission
│   ├── drone_example.cpp               # Applied multi-variable drone power telemetry
│   └── Beginner.c++                    # Direct ATmega328P bitwise register manipulation
│
├── Python/                             # Track B: AI, computational logic & high-level brain
│   ├── Lessons/
│   │   ├── lesson1.py                  # Rocket Bhaskaracharya Kinetic Energy & Momentum
│   │   ├── lesson2.py                  # Quadcopter Drone Lift-Thrust & Payload Calculator
│   │   ├── lesson3.py                  # Mars Lander Retro-Rocket Altitude & Velocity Cutoff
│   │   └── lesson4.py                  # Nuclear Reactor Core Thermal-Hydraulic Hazard Matrix
│   └── mds/                            # Blueprints, pedagogy, and progress trackers
│
└── Robotics/                           # Track C: Embedded circuits, microcontrollers & simulation
    ├── Robotics.ino                    # Non-blocking telemetry & state-machine firmware
    ├── CIRCUIT_PHYSICS_AND_POWER_GUIDE.md # Quantum LED physics, resistor math & power rails
    ├── diagram.json                    # Wokwi virtual hardware circuit schematic
    ├── wokwi.toml                      # Wokwi firmware simulation linker
    └── README.md                       # Electrical metrology & multimeter operations guide
```

---

## 🗺️ Visual Curriculum Progress

### Track A: C++ (Bits Directing Atoms)
```text
[██████████] Lesson 1: C++ Anatomy & Terminal Output (DONE)
[██████████] Lesson 2: Memory & Variables (DONE)
[██████████] Lesson 3: C++ Arithmetic & Science Equations (DONE)
[██████████] Lesson 4: Decimals in the Physical World (double) (DONE)
[██████████] Lesson 5: Interactive Inputs from Humans (std::cin) (DONE)
[██████████] Lesson 6: Decision Logic & Autonomous Branching (if / else) (DONE)
[██████████] Lesson 7: Multi-Condition Decision Chains (else if, &&, ||) (DONE)
[██████████] Lesson 8: Repetition & Loops (while) (DONE)
[██████████] Lesson 9: Counted Loops & Accumulators (for) (DONE)
[██████████] Lesson 10: Collections & Memory Arrays (double[]) (DONE)
[██████████] CAPSTONE SPRINT: 3-in-1 Master Aerospace Mission (DONE - 96/100)
----------------------------------------------------------------------------------------
[▓▓░░░░░░░░] Lesson 11: Modular Functions & Return Types (IN PROGRESS)
[░░░░░░░░░░] Lesson 12: Memory Pointers & Pass-by-Reference (&, *) (QUEUED)
```

### Track B: Python (AI & Computational Logic)
```text
[██████████] Lesson 1: Dynamic Variables, Scientific Formulas & f-strings (DONE - 100/100)
[██████████] Lesson 2: Interactive Dynamic Inputs & Type Casting (DONE - 100/100)
[██████████] Lesson 3: Decision Logic & Autonomous Control (DONE - 100/100)
[██████████] Lesson 4: Multi-Branch Sensor Fusion (elif, and, or) (DONE - 100/100)
[██████████] Lesson 5: Continuous Monitoring & Loops (while, break) (DONE - 100/100)
[██████████] Lesson 6: Counted Loops & Sequences (for, range) (DONE - 100/100)
[▓▓░░░░░░░░] Lesson 7: Dynamic Collections & Slicing (list, append) (UP NEXT)
[░░░░░░░░░░] Lesson 8: Reusable Mathematical Engines (def, Return Values) (QUEUED)
[░░░░░░░░░░] Lesson 9: Structured Key-Value Telemetry (dict, Nested JSON) (QUEUED)
[░░░░░░░░░░] Lesson 10: Matrix & Linear Algebra Primitives (Nested Lists) (QUEUED)
[░░░░░░░░░░] CAPSTONE SPRINT: 3-in-1 Master Autonomous Planetary Drone Mission (QUEUED)
```

---

## 🤖 The AI Mentor Protocol: Zero YouTube, Pure Mastery

You do **not** need 30-hour passive video tutorials, superficial bootcamps, or paid courses to master low-level systems and AI. All you need is **this repository** and an **AI Sparring Partner** (ChatGPT, Claude, Gemini, or Antigravity).

### How to Turn Any AI into Your Personal Systems Engineering Professor:

Copy and paste this master prompt into your AI model of choice:

```text
You are my strict, first-principles systems engineering and AI mentor (the "Big Bro" persona from https://github.com/shlokbuilder27/ai-engineering-journey). I reject vibe-coding, copy-pasting, and passive learning.

Follow this exact 3-stage protocol for each lesson in this repository:
1. Stage 1 (Memory & Silicon Model): Explain the core concept, its byte cost in RAM (Stack vs Heap), and why it matters in physics/robotics.
2. Stage 2 (Reference Architecture): Provide a clean, elegant reference implementation applied to aerospace/robotics.
3. Stage 3 (Novel Science Challenge): Give me an unfamiliar physical science problem (kinetics, orbital mechanics, circuits, nuclear safety) with strict specifications and an "Expected Output" box.

CRITICAL RULES FOR YOU:
- NEVER write the solution for Stage 3. Force my brain to write every single line.
- When I provide my code, review it with brutal honesty: test edge cases, check formatting, grade it out of 100, and only advance me when it executes with 100% precision.
```

By pairing an AI running this prompt with the problem sets and verified solutions in this repository, **any motivated student on Earth can gain world-class engineering mastery independently from their bedroom.**

---

## ⚡ Quickstart & Reproducibility

### 1. Compile & Run C++ Files
Requires GCC 13+ with C++23 support:
```powershell
g++ -std=c++23 C++/master.cpp -o C++/master.exe -lstdc++exp
./C++/master.exe
```

### 2. Run Python Lessons
Requires Python 3.10+:
```powershell
python Python/Lessons/lesson4.py
```

### 3. Run Robotics Simulation (Wokwi)
Open in Visual Studio Code with the **Wokwi Simulator** extension:
1. Hit `Ctrl + Shift + B` to compile `Robotics/Robotics.ino` via Arduino CLI.
2. Press `F1` $\rightarrow$ `Wokwi: Start Simulator` to run the interactive virtual Arduino Uno.

---

## 📜 License
Open-source under the [MIT License](LICENSE). Built for students, researchers, and engineers learning in public.
