def calculator():
    print("Welcome to the Calculator!")
    print("Select the operation you'd like to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        try:
            choice = int(input("\nEnter the number of your choice (1-5): "))
            if choice == 5:
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"The result of addition is: {num1 + num2}")
            elif choice == 2:
                print(f"The result of subtraction is: {num1 - num2}")
            elif choice == 3:
                print(f"The result of multiplication is: {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result of division is: {num1 / num2}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Run the calculator
calculator()