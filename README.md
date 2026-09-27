# Room Renting CLI System

## Overview

The Room Renting CLI System is a Python-based command-line application designed to demonstrate the basic working of a room/house renting system.

The system allows users to register and log in as either a Host or a Tenant. Hosts can add rental spots by providing details such as Spot ID, location, and price per day. Tenants can select an available spot, specify the number of days they want to rent it, calculate the total cost, and confirm the booking.

The project uses Python dictionaries and lists as an in-memory data store to maintain users, rental spots, and booking information during program execution.

## Features

### 1. User Registration

The system allows a new user to register by entering:

- Username
- Role (Host or Tenant)

After registration, the user information is stored in the in-memory users database.

### 2. User Login

Registered users can log in using their username.

If the username exists in the users database, the system displays a successful login message. If the username does not exist, the system displays a user-not-found message.

### 3. Add Rental Spot

A Host can add a rental spot by entering:

- Spot ID
- House/room location
- Price per day
- Host username


### 4. Display Available Spots

The system displays spots that are available.

For each available spot, it displays:

- Spot ID
- Location
- Price per day

### 5. Room Booking

A Tenant can enter:

- Tenant username
- Spot ID
- Number of days required

The system searches for the selected spot and checks whether it is available.

### 6. Cost Calculation

The total rental cost is calculated using:

    Total Cost = Price Per Day × Number of Days

The calculated amount is displayed before the booking is confirmed.

### 7. Booking Confirmation

The tenant can confirm or cancel the booking.

If the tenant confirms the booking:

- The rental spot is marked as unavailable.
- A booking record is created.
- The booking is stored in the bookings database.
- The total billed amount is displayed.

### 8. Final Database State

After the application finishes, the system displays the current contents of:

- Users database
- Rental spots database
- Bookings database

## Technologies and Tools Used

- Python 3
- Python dictionaries
- Python lists
- Command Line Interface (CLI)
- Modular Python files
- VS Code or any Python-compatible IDE
- Git and GitHub for source-code management

## Project Structure

```text
Room-Renting-CLI/
│
├── main.py
├── authentication.py
├── renting.py
├── booking_module.py
├── data_store.py
├── models.py
└── README.md
