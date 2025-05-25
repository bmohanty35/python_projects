# Employee Management System (EMS)

# Step 1 - Data Storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'IT', 'salary': 60000}
}


# Step 2 - Main Menu
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Step 3 - Add Employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print(f"Employee {name} added successfully!")
    except ValueError:
        print("Invalid input. Please enter correct data types.")


# Step 4 - View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print("\nID\tName\tAge\tDepartment\tSalary")
        print("-" * 50)
        for emp_id, details in employees.items():
            print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")


# Step 5 - Search for Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print(f"\nDetails of Employee ID {emp_id}:")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a valid Employee ID.")


# Run the EMS
if __name__ == "__main__":
    main_menu()