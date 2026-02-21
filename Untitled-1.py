def input_employee_details():
    """
    Function to input employee details from the user.
    Returns a dictionary with employee information.
    """
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    allowances = float(input("Enter allowances: "))
    return {
        "name": name,
        "basic_salary": basic_salary,
        "allowances": allowances
    }

def calculate_gross_salary(employee_details):
    """
    Function to calculate gross salary.
    Gross salary = basic salary + allowances
    """
    basic = employee_details["basic_salary"]
    allowances = employee_details["allowances"]
    gross = basic + allowances
    return gross

def calculate_deductions(employee_details, gross_salary):
    """
    Function to calculate deductions.
    Assuming deductions include tax (10% of gross) and insurance (fixed at 500).
    """
    tax = 0.10 * gross_salary
    insurance = 500.0
    total_deductions = tax + insurance
    return total_deductions

def display_final_salary(employee_details, gross_salary, deductions):
    """
    Function to display the final salary details.
    """
    net_salary = gross_salary - deductions
    print("\n--- Employee Salary Details ---")
    print(f"Name: {employee_details['name']}")
    print(f"Basic Salary: {employee_details['basic_salary']:.2f}")
    print(f"Allowances: {employee_details['allowances']:.2f}")
    print(f"Gross Salary: {gross_salary:.2f}")
    print(f"Deductions: {deductions:.2f}")
    print(f"Net Salary: {net_salary:.2f}")

def main():
    """
    Main function to run the salary calculator application.
    """
    print("Welcome to Employee Salary Calculator")
    employee = input_employee_details()
    gross = calculate_gross_salary(employee)
    deductions = calculate_deductions(employee, gross)
    display_final_salary(employee, gross, deductions)

if __name__ == "__main__":
    main()
    