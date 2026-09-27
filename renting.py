import data_store

print("\n--- Rent Management ---")
print("[Add a Spot]")

host_name = input("Enter Host username adding the spot: ")
spot_id_input = input("Enter a unique Spot ID (integer): ")
location_input = input("Enter house location: ")
price_input = input("Enter price per day: ")

spot_id = int(spot_id_input)
price_per_day = float(price_input)

new_spot = {
    "spot_id": spot_id,
    "location": location_input,
    "price_per_day": price_per_day,
    "host_username": host_name,
    "is_available": True
}

data_store.spots_db.append(new_spot)
print("House added successfully!")

print("\n[Available Spots]")
for spot in data_store.spots_db:
    if spot["is_available"]:
        print(
            "Spot ID:", spot["spot_id"],
            "| Location:", spot["location"],
            "| Price: Rs", spot["price_per_day"]
        )
