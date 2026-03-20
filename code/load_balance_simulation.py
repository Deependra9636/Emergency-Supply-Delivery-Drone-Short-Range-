# load_balance_simulation.py

def motor_load(throttle, imbalance):
    m1 = throttle + imbalance
    m2 = throttle - imbalance
    m3 = throttle + imbalance
    m4 = throttle - imbalance

    return m1, m2, m3, m4

throttle = 1500
imbalance = 50

motors = motor_load(throttle, imbalance)

print("Motor Loads:", motors)
