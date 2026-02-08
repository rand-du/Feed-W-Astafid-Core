# 💛 Feed-W-Astafid: AI Logic for Sustainability
# ☀️ Concept: Predicting surplus to feed the community

def predict_and_donate(production_kg, expected_demand_kg):
    # Core Logic: Calculating the surplus
    surplus = production_kg - expected_demand_kg
    
    if surplus > 0:
        print(f"✨ Alert: Potential waste of {surplus}kg detected.")
        print(f"💛 Action: Notifying nearby Charities to collect {surplus}kg.")
    else:
        print("☀️ Perfect Balance: Production matches demand. No waste!")

# Simulation: Example for a local restaurant
print("--- Feed-W-Astafid AI Monitor ---")
predict_and_donate(production_kg=150, expected_demand_kg=120)
