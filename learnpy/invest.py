#Write a script invest.py that will track the growing amount of an investment over time.
#This script includes an invest() function that takes three inputs: the initial investment
#amount, the annual compounding rate, and the total number of years to invest. So, the
#first line of the function will look like this:
#def invest(amount, rate, time):
#The function then prints out the amount of the investment for every year of the time
#period.
#In the main body of the script (after defining the function), use the following code to test
#your function:
#invest(100, .05, 8)
#invest(2000, .025, 5)


def invest(amount, rate, time):
    principal = amount
    for n in range(1, time+1):
        interest_amount = rate * principal
        principal = principal + interest_amount
        print(f"Interest after {n} years is {interest_amount} with a total {principal}")

invest(100, 0.05, 8)
invest(2000, .025, 5)