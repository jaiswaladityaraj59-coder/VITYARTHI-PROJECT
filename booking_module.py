import data_store

print("Booking Engine")

tenant_name = input("Enter tenant username: ")
book_spot_id_input = input("Enter Spot ID to book: ")
days_input = input("Enter duration in days: ")

book_spot_id = int(book_spot_id_input)
days = int(days_input)

selected_spot = {}

for spot in data_store.spots_db:
    if spot["spot_id"] == book_spot_id and spot["is_available"]:
        selected_spot = spot
        break

if selected_spot:
    total_cost = selected_spot["price_per_day"] * days
    print("Total Cost for", days, "days: Rs", total_cost)

    confirm = input("Confirm booking? (Y/N): ")

    if confirm.lower() == "y":
        selected_spot["is_available"] = False

        new_booking = {
            "spot_id": book_spot_id,
            "tenant_username": tenant_name,
            "days": days,
            "total_cost": total_cost
        }

        data_store.bookings_db.append(new_booking)
        print("Booking confirmed! Total billed: Rs", total_cost)
    else:
        print("Booking cancelled.")
else:
    print("Spot is unavailable or does not exist.")
