import sys

def calculate_bonus(present_days):
    if present_days >= 26:
        return 5000
    elif present_days >= 20:
        return 3000
    elif present_days >= 15:
        return 1500
    else:
        return 0

print("=== Employee Bonus Calculator ===")

try:
    # ✔ If values are passed from Jenkins / command line
    if len(sys.argv) == 4:
        emp_id = int(sys.argv[1])
        name = sys.argv[2]
        present_days = int(sys.argv[3])

    # ✔ Else ask user manually (local run)
    else:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        present_days = int(input("Enter Present Days: "))

    bonus = calculate_bonus(present_days)

    print("\n--- Employee Details ---")
    print("Employee ID:", emp_id)
    print("Employee Name:", name)
    print("Present Days:", present_days)
    print("Bonus:", bonus)

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
