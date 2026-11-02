# Smart Fire & Smoke Detection Agent

print(" SMART FIRE & SMOKE DETECTION AGENT ")

# User inputs
temperature = float(input("Enter temperature (°C): "))
smoke = input("Is smoke detected? (yes/no): ").lower()
flame = input("Is flame detected? (yes/no): ").lower()
gas = input("Is dangerous gas detected? (yes/no): ").lower()
print("\nAgent Analysis")
# Convert inputs to Boolean
smoke_detected = smoke == "yes"
flame_detected = flame == "yes"
gas_detected = gas == "yes"

# Agent decision-making
if flame_detected and smoke_detected and temperature >= 50:
    status = "CONFIRMED FIRE"
    actions = [
        "Activate fire alarm",
        "Activate sprinkler system",
        "Cut off electrical supply",
        "Turn on emergency lights",
        "Unlock emergency exits",
        "Send emergency notification"
    ]

elif smoke_detected and temperature >= 40:
    status = "HIGH FIRE RISK"
    actions = [
        "Activate warning alarm",
        "Increase monitoring",
        "Notify building security"
    ]

elif gas_detected and temperature >= 35:
    status = "DANGEROUS GAS / FIRE RISK"
    actions = [
        "Activate gas warning alarm",
        "Turn off electrical equipment",
        "Notify building security"
    ]

elif smoke_detected:
    status = "POSSIBLE FIRE / SMOKE DETECTED"
    actions = [
        "Activate warning alarm",
        "Increase sensor monitoring",
        "Check the affected area"
    ]

elif temperature >= 40:
    status = "HIGH TEMPERATURE"
    actions = [
        "Increase monitoring",
        "Notify building security"
    ]

else:
    status = "NORMAL"
    actions = [
        "Continue monitoring"
    ]

# Display result
print("AGENT DECISION:", status)

print("\nActions taken by the agent:")
for action in actions:
    print("→", action)
