def print_right_triangle():
    try:
        height = int(input("Enter the height of the triangle: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == "__main__":
    print_right_triangle()
