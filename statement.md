# Room Renting CLI System - Statement

## 1. Problem Statement

It helps in Managing rental rooms or houses and involves maintaining information about available rental properties, their locations, prices, hosts, tenants, and bookings. A simple system is required to organize this information and make the basic rental and booking process easier to manage.

The Room Renting CLI System is a Python-based command-line application developed to provide a solution for managing rental spots and bookings. The system allows users to register and log in, hosts to add rental spots and tenants to book available rental spots for a specified number of days.

The system calculates the total rental cost based on the daily rental price and number of days. Once a booking is confirmed, the selected rental spot is marked as unavailable and the booking information is stored.

The project demonstrates the use of Python programming concepts such as modules, dictionaries, lists, loops, conditional statements, user input, and basic data management.

## 2. Scope of the Project

This project covers the basic operations required for a simple room renting system through a command-line interface.

The system includes:

- User registration
- User login
- Host and Tenant roles
- Adding rental spots
- Storing rental spot information
- Displaying available rental spots
- Selecting a rental spot using Spot ID
- Specifying the rental duration
- Calculating the total rental cost
- Confirming or cancelling a booking
- Updating the availability of a rental spot
- Storing booking information
- Displaying the final application data

The project currently uses Python dictionaries and lists as an in-memory data store. User information is stored in `users_db`, rental spots are stored in `spots_db`, and booking records are stored in `bookings_db`.

The current scope does not include a permanent external database, graphical user interface, online payment system, or web-based access.

## 3. Target Users

### Hosts

Hosts are users who provide rooms or houses for rent.

Hosts can:

- Register in the system
- Log in using their username
- Add a rental spot
- Enter the rental location
- Set the price per day
- Make the rental spot available for booking

### Tenants

Tenants are users who want to rent an available room or house.

Tenants can:

- Register in the system
- Log in using their username
- Select an available rental spot
- Enter the Spot ID
- Specify the number of rental days
- View the calculated rental cost
- Confirm or cancel a booking


## 4. High-Level Features

### 4.1 User Registration

Users can register by entering a username and selecting a role as Host or Tenant. The user information is stored in the application's in-memory user database.

### 4.2 User Login

The system checks whether the entered username exists in the user database. If the username exists, the user is logged in successfully.

### 4.3 Rental Spot Management

A Host can add a rental spot by providing:

- Spot ID
- Location
- Price per day
- Host username

The newly added rental spot is initially marked as available.

### 4.4 Available Rental Spots

The system checks the rental spots stored in the application and displays the spots that are currently available, including their Spot ID, location, and price per day.

### 4.5 Room Booking

A Tenant can select an available rental spot using its Spot ID and enter the number of days for which the room is required.

### 4.6 Rental Cost Calculation

The system automatically calculates the total rental cost using:

    Total Cost = Price Per Day × Number of Days

### 4.7 Booking Confirmation

Before completing a booking, the Tenant is asked to confirm the booking.

If the Tenant confirms:

- The rental spot is marked as unavailable.
- A booking record is created.
- The booking is added to the bookings database.
- The total billed amount is displayed.

If the Tenant cancels, the booking is not created.

### 4.8 In-Memory Data Management

The application maintains three main data structures:

- `users_db` - stores user information
- `spots_db` - stores rental spot information
- `bookings_db` - stores booking information


### 4.9 Modular Project Structure

The project is divided into separate Python files for different responsibilities:

- `main.py` - starts and coordinates the application
- `authentication.py` - handles registration and login
- `renting.py` - handles rental spot creation and available spots
- `booking_module.py` - handles the booking process
- `data_store.py` - maintains the in-memory application data
- `models.py` - contains the basic data-model representation