#🔋 Scenario: Electric Autonomous Rover Fast-Charging Station
battery_pct = float(input("Enter initial battery percentage (e.g. 15.0): "))
charge_rate = float(input("Enter charge rate per cycle (e.g. 20.0): "))
cycle_count = 0
while battery_pct < 100.0:
    cycle_count += 1
    battery_pct += charge_rate
    if battery_pct > 100.0:
        battery_pct = 100.0
    print(f"Cycle {cycle_count}: Battery charged to {battery_pct:.1f}%.")
print(f"[CHARGING COMPLETE] Battery fully recharged to {battery_pct:.1f}% in {cycle_count} cycles. Undocking rover!")
