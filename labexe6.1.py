def generate_multiplication_table():
    try:
        number = int(input("Enter the number for the multiplication table: "))
        limit = int(input("Enter the limit up to which you want the table: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return
    
    print(f"\nMultiplication table for {number} up to {limit}:\n")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    generate_multiplication_table()
