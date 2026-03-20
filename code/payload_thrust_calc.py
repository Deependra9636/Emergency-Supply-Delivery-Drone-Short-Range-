# payload_thrust_calc.py

def required_thrust(weight_kg):
    g = 9.81
    thrust = weight_kg * g
    return thrust

drone_weight = 1.2
payload_weight = 0.3

total_weight = drone_weight + payload_weight

print("Total Weight:", total_weight, "kg")
print("Required Thrust:", required_thrust(total_weight), "N")
