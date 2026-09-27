print("=== Welcome to Room Renting CLI ===")

import data_store
import authentication
import renting
import booking_module

print("\n=== Application Execution Complete ===")
print("\n[Final Database States]")
print("Users in DataBase:", data_store.users_db)
print("Spots in DataBase:", data_store.spots_db)
print("Bookings in DataBase:", data_store.bookings_db)