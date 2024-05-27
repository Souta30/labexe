# Ask the user to input their age
age = int(input("Please enter your age: "))

# Ask the user if they are a student or not
student_status = input("Are you a student? (yes/no): ").lower()

# Use logical operators to determine eligibility for discount
if age <= 12:
    print("You are eligible for a discount.")
elif age >= 13 and age <= 18 and student_status == "yes":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
