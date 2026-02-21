class Employee:
    def __init__(self, employee_name, employee_id, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = salary
    
    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by: ${amount}. New salary: ${self.salary}")
        else:
            print("Invalid amount! Salary increase must be positive.")
    
    def display_details(self):
        print(f"Employee Name: {self.employee_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


# Create an object and test the methods
employee = Employee("Noyal mathew", "EMP001", 50000)

# Display initial employee details
print("=== Initial Employee Details ===")
employee.display_details()

# Increase salary
print("\n=== After Salary Increase ===")
employee.increase_salary(10000)

# Display updated details
print("\n=== Final Employee Details ===")
employee.display_details()
