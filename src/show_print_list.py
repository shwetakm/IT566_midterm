
def display_list(list_numbers):
     print("Entered numbers are: ", list_numbers)

def show_print_list():
    print("Enter show: to print the list | exit: to exit the program ")
    input_flag = True
    list_numbers = []
    while input_flag:
        numbers_input = input("Please enter your input to add to the list: ")

        if numbers_input == "show":
           display_list(list_numbers)
        elif numbers_input == "exit":
           input_flag =False
           print("Exiting the program")
        else:
            try:
                list_numbers.append(numbers_input)
            except ValueError:
                print("Invalid input, please enter a valid text to add/ show/ exit")
    return;

     
        
        
    
