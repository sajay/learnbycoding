#Write a script called exponent.py that receives two numbers from the user and displays
#the result of taking the first number to the power of the second number. A sample run of
#the program should look like this (with example input that has been provided by the user
#included below):

base_number = input("Enter the base number ")

exponent = input("Enter the power : ")

print("Entered base is {} & entered exponent is {}".format(base_number, exponent))

new_value = float(base_number) ** int(exponent)

print(f"Result is {new_value}")

