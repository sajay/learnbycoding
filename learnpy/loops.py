#Write a for loop that prints out the integers 2 through 10, each on a new line, by
#using the range() function
#2. Use a while loop that prints out the integers 2 through 10 (Hint: you'll need to
#create a new integer first; there isn't a good reason to use a while loop instead of a
#for loop in this case, but it's good practice...)
#3. Write a function called doubles() that takes one number as its input and doubles
#that number three times using a loop, displaying each result on a separate line; test
#your function by calling doubles(2) to display 4, 8, and 16

for n in range(2,11):
    print(n)

n=2
while(n <= 10):
    print(n)
    n=n+1

def doubles(number):
    doubled_num = number
    for n in range(1, 4):
        doubled_num = 2 * doubled_num
        print(f"Doubled Num {n} is {doubled_num}")
         
doubles(2)