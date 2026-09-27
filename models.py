print("\nInitialize Application Data")

print("\n[User Configuration]")
user_username = input("Enter a username: ")
user_role = input("Enter role (Host or tenant): ")

current_user = {
    "username": user_username,
    "role": user_role
}

print("\n[Rent Configuration]")
spot_id_input = input("Enter a unique Spot ID (integer): ")
spot_location = input("Enter location description: ")
spot_price_input = input("Enter price per day: ")

room_spot = {
    "spot_id": int(spot_id_input),
    "location": spot_location,
    "price_per_day": float(spot_price_input),
    "host_username": user_username,
    "is_available": True
}

print("\n[Booking Configuration]")
tenant_name = input("Enter tenant username booking this spot: ")
days_input = input("Enter number of days needed: ")
booking_days = int(days_input)

calculated_total_cost = room_spot["price_per_day"] * booking_days

booking_record = {
    "spot_id": room_spot["spot_id"],
    "tenant_username": tenant_name,
    "days": booking_days,
    "total_cost": calculated_total_cost
}

print("\nSummary of Captured Data")
print("User Model:", current_user)
print("Spot Model:", room_spot)
print("Booking Model:", booking_record)
