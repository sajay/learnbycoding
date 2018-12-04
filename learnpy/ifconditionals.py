#Write a script that prompts the user to enter a word using the input() function,
#stores that input in a variable, and then displays whether the length of that string is
#less than 5 characters, greater than 5 characters, or equal to 5 characters by using
#a set of if , elif and else statements.

user_str = input("Enter a word")

if(len(user_str) < 5):
    print(f"The length of {user_str} is <5 {len(user_str)}")
elif(len(user_str) > 5):
    print(f"The length of {user_str} > 5 : {len(user_str)}")
else:
    print(f"The length of {user_str} = 5 : {len(user_str)}")
    