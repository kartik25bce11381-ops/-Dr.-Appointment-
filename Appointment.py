# Simple console-based doctor appointment app for beginners

doctors = ["Dr. Sharma", "Dr. Rao", "Dr. Khan", "Dr. Mehta", "Dr. Gupta", "Dr. Iyer", "Dr. Singh"]
appointments = []
fees = {}
fees["Dr. Sharma"] = 500
fees["Dr. Rao"] = 600 
fees["Dr. Khan"] = 700
fees["Dr. Mehta"] = 550 
fees["Dr. Gupta"] = 650
fees["Dr. Iyer"] = 750  
fees["Dr. Singh"] = 800


def show_doctors():
    print("Available Doctors:")
    for i, doc in enumerate(doctors, start=1):
        print(f"{i}. {doc}")

def book_appointment():
    patient_name = input("Enter your name: ")
    show_doctors()
    choice = int(input("Select doctor by number: "))
    if 1 <= choice <= len(doctors):
        doctor = doctors[choice - 1]
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")
        appointment = {"patient": patient_name, "doctor": doctor, "date": date, "time": time}
        appointments.append(appointment)
        print("Appointment booked successfully!")
    else:
        print("Invalid doctor selection.")

def view_appointments():
    print("\nAll Appointments:")
    if not appointments:
        print("No appointments booked yet.")
    else:
        for appt in appointments:
            print(f"{appt['patient']} with {appt['doctor']} on {appt['date']} at {appt['time']}")

def main():
    while True:
        print("\nDoctor Appointment System")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            print("Thanks for using the system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
