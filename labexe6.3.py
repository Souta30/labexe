def print_numbers_with_conditions():
    for outer in range(1, 10):
        if outer == 7:
            print("Reached 7, breaking outer")
            break
        for inner in range(1, 10):
            if inner == 3:
                print("Skipping 3 in the inner loop")
                continue
            print(inner)
        print()  # Add a new line after each iteration of the inner loop

if __name__ == "__main__":
    print_numbers_with_conditions()
