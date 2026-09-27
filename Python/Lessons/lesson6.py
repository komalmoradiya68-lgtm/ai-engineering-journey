#🛰️ Scenario: Deep-Space CubeSat Orbital Solar Flux Accumulator
start_deg = int(input("Enter starting orbital angle (deg): "))
end_deg = int(input("Enter ending orbital angle (deg): "))
step_deg = int(input("Enter sample step angle (deg): "))
flux_rate = float(input("Enter flux factor (W/deg): "))
total_flux = 0.0
for angle in range(start_deg, end_deg + 1, step_deg):
    sample_flux = angle * flux_rate
    total_flux += sample_flux
    print(f"Angle {angle} deg: Measured flux = {sample_flux:.1f} W")
print(f"[ORBITAL PASS COMPLETE] Total Solar Energy Collected: {total_flux:.2f} Joules.")
