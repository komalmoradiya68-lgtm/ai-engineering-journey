#🚁 Scenario: Quadcopter Drone Lift-Thrust & Payload Calculator
drone_name = input("Enter drone designation: ")
dry_frame_mass = float(input("Enter the dry frame mass: "))
cargo_payload_mass = float(input("Enter the cargo payload mass: "))
total_mass = dry_frame_mass + cargo_payload_mass
hover_thrust = total_mass * 9.8
thrust_per_motor = hover_thrust / 4
print(f"{drone_name} has an airborne mass of {total_mass:.2f} kg with total hover thrust of {hover_thrust:.2f} N and minimum thrust of {thrust_per_motor:.2f} N.")
