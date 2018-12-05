#Write a script that uses the randint() function to simulate the toss of a die,
#returning a random number between 1 and 6.
#2. Write a script that simulates 10,000 throws of dice and displays the average number
#resulting from these tosses.

from random import randint

die_toss_result = randint(1,6)

toss_value_sum = 0
for n in range(1,10001):
    toss_value_sum = toss_value_sum + randint(1,6)
print(f"Average after 10000 tosses : {toss_value_sum/10000}")
    