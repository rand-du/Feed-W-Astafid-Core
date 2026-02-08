# Feed-W-Astafid Project
# Initial logic for tracking food surplus and optimizing donations

def calculate_food_status():
    """
    Function to calculate the difference between daily production and demand.
    It suggests an action based on the result.
    """
    print("--- Feed-W-Astafid Inventory System ---")
    
    try:
        # Input section: Using clear and professional variable names
        daily_production = float(input("Enter total production amount (kg): "))
        actual_demand = float(input("Enter actual demand/sales amount (kg): "))
        
        # Logic: Simple subtraction to find the surplus
        surplus = daily_production - actual_demand
        
        print("\nAnalysis Result:")
        print("-" * 20)
        
        if surplus > 0:
            print(f"Status: Surplus of {surplus}kg detected.")
            print("Action: Redirecting extra food to the donation network.")
        elif surplus == 0:
            print("Status: Equilibrium achieved.")
            print("Action: No further action required.")
        else:
            deficit = abs(surplus)
            print(f"Status: Deficit of {deficit}kg.")
            print("Action: Review supply chain for shortages.")
            
    except ValueError:
        # Handling non-numeric inputs professionally
        print("Error: Invalid input. Please enter numerical values for weights.")

# Execute the system
if __name__ == "__main__":
    calculate_food_status()
