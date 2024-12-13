# Constants for room rates
room_rates = {
    "Standard": 100,
    "Deluxe": 150,
    "Suite": 250
}

# User inputs
room_type = input("Enter the room type (Standard, Deluxe, Suite): ")
nights = int(input("Enter the number of nights: "))
season = input("Enter the season (Peak, Off, Regular): ")
is_loyalty_member = input("Are you a loyalty member (Yes, No)? ")


base_cost = room_rates[room_type] * nights


if nights > 7:
    discount = 0.20  
elif nights > 3:
    discount = 0.10 
else:
    discount = 0

if season == "Peak":
    seasonal_adjustment = 0.20  
elif season == "Off":
    seasonal_adjustment = -0.15  
else:
    seasonal_adjustment = 0  


if is_loyalty_member == "Yes":
    loyalty_discount = 0.05 
else:
    loyalty_discount = 0

# Calculate total cost
total_cost = base_cost
total_cost -= total_cost * discount  
total_cost += total_cost * seasonal_adjustment 
total_cost -= total_cost * loyalty_discount  

# Output the final booking cost
print(f"The final booking cost is: ${total_cost:.2f}")
# Enter the room type (Standard, Deluxe, Suite): Deluxe
# Enter the number of nights: 1
# Enter the season (Peak, Off, Regular): Off
# Are you a loyalty member (Yes, No)? Yes
# The final booking cost is: $121.12