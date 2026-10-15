def display_sum_numbers(numbers_list):
    print("Sum of the enetered numbers is: ", sum(numbers_list))


def sum_input_numbers():
    print("Enter a number to add to the list | sum: display the sum | quit: to exit the program")
    numbers_list = []
    input_flag = True

    while input_flag:
        number_input = input("Enter a number:")
        if number_input == "sum":
            display_sum_numbers(numbers_list)
        elif number_input == "q":
            input_flag = False
            print("Exiting the program")
        else:
            try:
                numbers_list.append(float(number_input))
            except ValueError:
                print("Invalid input")