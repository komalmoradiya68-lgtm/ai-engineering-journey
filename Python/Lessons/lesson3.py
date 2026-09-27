#🪐 Scenario: Mars Lander Retro-Rocket Cutoff Controller
altitude_m = float(input("Enter radar altitude (m): "))

velocity_mps = float(input("Enter descent velocity (m/s): "))

if altitude_m <= 2.0:  
    if velocity_mps <= 1.5:
        print("[SUCCESS] Soft touchdown confirmed! Retro-rockets CUT OFF.")
    else:
        print("[CRITICAL WARNING] Hard impact! Velocity exceeded safe limit! Deploying emergency airbags!")
else:
    print(f"[DESCENT PHASE ACTIVE] Altitude: {altitude_m} m. Retro-thrusters firing at full throttle.")