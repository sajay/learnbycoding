#Use a break statement to write a script that prompts the users for input repeatedly,
#only ending when the user types "q" or "Q" to quit the program; a common way of
#creating an infinite loop is to write while True: .
#2. Combine a for loop over a range() of numbers with the continue keyword to
#print every number from 1 through 50 except for multiples of 3; you will need to use
#the % operator.

while(True):
    user_input = input("Enter an input")
    if(user_input == "q" or user_input == "Q"):
        break

for n in range(1,50):
    if((n % 3) != 0):
        print(f"{n} is NOT divisible by 3")
    else:
        continue
        