# delivery_drop_logic.py

def drop_payload(distance):
    if distance < 2:
        return "Dropping payload"
    else:
        return "Continue flying"

distance = 1.5

print(drop_payload(distance))
