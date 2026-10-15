
def display_list(list_numbers):
     print("Entered numbers are: ", list_numbers)

def show_print_list():
    print("Enter print: to print the list of numbers | quit: to exit the program ")
    input_flag = True
    list_numbers = []
    while input_flag:
        numbers_input = input("Please enter a number to add to the list: ")

        if numbers_input == "print":
           display_list(list_numbers)
        elif numbers_input == "quit":
           input_flag =False
           print("Exiting the program")
        else:
            try:
                list_numbers.append(int(numbers_input))
            except ValueError:
                print("Invalid input, please enter a number/ print/ quit")
    return;

     
        
        
    
