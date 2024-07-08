import csv

tables = [
    {
        "number": 1, "seats": 4,
    },
    {
        "number": 2, "seats": 3,
    },
    {
        "number": 3, "seats": 6,
    },
     {
        "number": 4, "seats": 5,
    },
]


reservation_file = 'reservation.csv'
def make_reservation(tables, reservation_file):
    name = input("Enter your name: ")
    contact = input("Enter your address: ")
    party_size = int(input("Enter number of people: "))
    date = input("Enter date YYYY-MM-DD: ")
    start_time = input("Enter start time HH:MM: ")
    end_time = input("Enter end time HH:MM: ")

    available_tables= [table for table in tables if table["seats"] >= party_size]
    if not available_tables:
        print("table is not available")
        return
    
    table_number= int(input("Enter table_number: "))
    if table_number not in [table["number"] for table in available_tables]:
        print("invalid table number")
        return
    new_row = [table_number, name, party_size, date, start_time, end_time]
    header = ['table_number', 'name', 'party_size', 'date', 'start_time', 'end_time']

    with open(reservation_file, mode = "a", newline="") as file:
        writer = csv.writer(file)
        if not header:
            writer.writerow(header)
        writer.writerow(new_row)
        print(header)
        print(f"Table {table_number} reserved successfully for {name} on {date}")
# make_reservation(tables, reservation_file)

def view_reservation(reservation_file):
    try:
        with open(reservation_file, "r") as file:
            reader = csv.reader(file)
            reservations = list(reader)
            for reservation in reservations:
                print(reservation)      
    except Exception as e:
        print("Error found")
        pass
# view_reservation(reservation_file)

def daily_summary(reservation_file):
    date = input("Enter date of reservation: ")
    try:
        with open(reservation_file, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
            correct_reservations = [row for row in reservations if row[header.index("date")] == date]
            if correct_reservations:
                for i in correct_reservations:
                    print(i)
            else:
                print("No reservation found")
    except Exception as e:
        print('Invalid date')
        pass
# daily_summary(reservation_file)



def modify_reservation(reservation_file):
    date = input("Enter the date of the reservation to modify (format: YYYY-MM-DD): ")
    name = input("Enter the name of the reservation to modify: ")
    # table_number = input("Enter the table number of the reservation to modify: ")

    try:
        # Read all reservations
        with open(reservation_file, "r", newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
        
        # Find and modify the reservation
        for row in reservations:
            if row[header.index("date")] == date and row[header.index("name")] == name:
                print("Current reservation details:", row)
                
                # Update the fields
                new_name = input(f"Enter new name (leave blank to keep current value '{row[header.index('name')]}'): ")
                if new_name:
                    row[header.index('name')] = new_name

                # new_table_number = input(f"Enter new table number (leave blank to keep current value '{row[header.index('table_number')]}'): ")
                # if new_table_number:
                #     row[header.index('table_number')] = new_table_number

                new_date = input(f"Enter new date (leave blank to keep current value '{row[header.index('date')]}'): ")
                if new_date:
                    row[header.index('date')] = new_date
                
                # Write the updated reservations back to the CSV file
                with open(reservation_file, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(reservations)

                print("Reservation updated successfully.")
                return  # Exit function after updating

        # If no reservation was found
        print("No reservation found for the given details.")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# modify_reservation(reservation_file)