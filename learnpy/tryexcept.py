#Write a script that repeatedly asks the user to input an integer, displaying a
#message to "try again" by catching the ValueError that is raised if the user did not
#enter an integer; once the user enters an integer, the program should display the
#number back to the user and end without crashing

while(True):
    try:
        input_number = int(input("Enter an integer :"))
        print(f"You entered an integer {input_number}")
        break
    except ValueError :
        print("You did not enter an integer ")
        continue