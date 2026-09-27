#⚛️ Scenario: Nuclear Reactor Core Thermal-Hydraulic Safety System
temp_c = float(input("Enter coolant temperature (C): "))
pressure_bar = float(input("Enter loop pressure (bar): "))
if temp_c >= 350.0 or pressure_bar >= 160.0:
    print ("[ALERT LEVEL: RED] CRITICAL HAZARD! Automated SCRAM shutdown initiated!")
#Rule 2 (Elevated Warning):
elif temp_c >= 300.0 and pressure_bar >= 130.0:
    print ("[ALERT LEVEL: YELLOW] WARNING! High thermal stress. Engaging auxiliary coolant pumps.")
#Rule 3 (Sub-optimal Low Temperature):
elif temp_c < 250.0:
    print("[ALERT LEVEL: BLUE] Sub-optimal temperature. Increasing control rod extraction.")
#Rule 4 (Nominal Baseline):
else:
    print("[ALERT LEVEL: GREEN] Reactor core operating within nominal baseline parameters.")