"""Add fuel calculator, autarkie calculator, and visual polish to the app."""

# Read current data.json and add fuel/autarkie config
import json
with open("data.json") as f:
    data = json.load(f)

# Add fuel config
data["fuel"] = {
    "consumption": 10.5,  # L/100km for T5 Multivan with Dachzelt
    "type": "diesel",
    "prices": {  # €/L average 2026
        "Deutschland": 1.65,
        "Österreich": 1.55,
        "Schweiz": 1.80,
        "Italien": 1.75,
        "Frankreich": 1.70,
        "Slowenien": 1.55,
        "Kroatien": 1.50,
        "Spanien": 1.55,
        "Niederlande": 1.90,
    }
}

# Add autarkie config
data["autarkie"] = {
    "battery_ah": 100,  # LiFePO4 Ah
    "battery_v": 12.8,
    "solar_watt": 400,  # W peak
    "solar_hours": 4,  # effective sun hours/day
    "water_liters": 30,  # Tank size
    "water_per_day": 8,  # L per person/day * 4 persons
    "consumption_watts": 150,  # average W consumption (fridge, lights, charging)
}

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Data updated with fuel + autarkie config")
