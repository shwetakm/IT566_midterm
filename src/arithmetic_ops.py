def arithmetic_ops():
    number1 = input("Enter the first number to proceed the calculation: ")

    input_flag = True
    while input_flag:
        math_op = input("Enter the arithmetic operators (+, -, *, /) to perform the calculation | q: to exit the program: ")
        if math_op == "q":
            input_flag = False
            print("Exiting the program")
        elif math_op  in ["+", "-", "*", "/"]:
            number2 = input("Enter the second number to proceed the calculation: ")
            try:
                match math_op:
                    case "+":
                        number1 = float(number1) + float(number2)
                        print(number1)
                    case "-":
                        number1 = float(number1) - float(number2)
                        print(number1)
                    case "*":
                        number1 = float(number1) * float(number2)
                        print(number1)
                    case "/":
                        number1 = float(number1) / float(number2)
                        print(number1)
                    case "q":
                        input_flag = False
                        print("Exiting the program")
            except ValueError:
                print("Invalid input")
        else:
            print("Invalid input")