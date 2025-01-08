def calculator():
    print("Basic Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    result = None
    while True:
        if result is None:
            num1 = float(input("Enter first number: "))
        else:
            use_result = input(f"Current result is {result}. Do you want to use it? (yes/no): ").lower()
            if use_result == 'yes':
                num1 = result
            else:
                num1 = float(input("Enter new first number: "))

        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue

            print(f"Result: {result}")
        else:
            print("Invalid input. Please choose a valid operation.")

        next_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

calculator()
