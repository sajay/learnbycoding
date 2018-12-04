
#string methods
#find is case sensitive and finds the 1st occurance of that substring
long_string = " This is a very very long string in a program"
result1 = long_string.find("very");

print(f"The result of find is {result1}")

print("Finding directly".find("direct"))

#replace

my_string = "I'm telling you the truth; he speaks only the truth"
print(my_string.replace("the truth", "lies"))

#replace abovev didnt change the string. Need to reassign

my_string = my_string.replace("the truth", "lies")

print(f"My string after replaceis {my_string}")

#1.In one line, display the result of trying to find() the substring "a" in the string
#"AAA"; the result should be -1

print("AAA".find("a"))

#2. Create a string object that contains the value "version 2.0"; find() the first
#occurrence of the number 2.0 inside of this string by first creating a "float" object that
#stores the value 2.0 as a floating-point number, then converting that object to a
#string using the str() function

initial_value = "version 2.0"
float val_in_string = 2.0;
float_as_str = str(val_in_string)

print(f"Find result is : {initial_value.find(float_as_str)}")



#3. Write and test a script that accepts user input using input() , then displays the
#result of trying to find() a particular letter in that input
#Find a String in a String

user_input = input("Hello: Please enter a string as input")
print(f"The user entered {user_input}")

print(f"Result of finding from user input {user_input.find("name")}")

