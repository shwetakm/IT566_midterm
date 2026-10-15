def show_reverse_string(str_to_reverse):
  end = len(str_to_reverse) -1
  final_string =""
  while end >=0:
    final_string = final_string + str_to_reverse[end]
    end = end -1
  print("Reversed string: ", final_string)
  return 


def reverse_text():
    input_flag = True
    print("Enter a string to reverse | exit: to exit the program.")
    while input_flag:
     str_to_reverse = input("Enter your string to reverse: ")
     if str_to_reverse == "exit":
       input_flag = False
       print("Exiting the program.")
     else:
        show_reverse_string(str_to_reverse)
    return
