# battery_impact.py

def battery_usage(base_usage, payload_factor):
    return base_usage * payload_factor

base = 100
payload_factor = 1.3

print("Battery Consumption:", battery_usage(base, payload_factor))
