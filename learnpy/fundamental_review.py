#Copy and paste the code below to IDLE and save it as fundamental_review.py.
#2. Run the file. All print statements in Part 1 return False and there is a TypeError
#in Part 2.
#3. Modify the variables so that all of the print statements return True .
#print "\n# -- part 1 -- #"
# Modify the variable value so that all of the
# `print` statements return `True`.

zero = 1
one = 2
two = [5, 4, 3, 2, 1, 0]
three = "I love Python!"
four = [["P", "y", "t", "h", "o", "n"],["i", "s"],["h", "a", "r", "d"]]
five = {"happy":"birthday"}
six = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
days = ("Fri", "Sat", "Sun")
x, y, seven = days

# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# -------------------------------------- #
print("zero: {}".format(zero == 0))
print("one: {}".format(one > 22))
print("two: {}".format(len(two) == 5))
print("three: {}".format(three[2] == "Python!"))
print("four: {}".format()
four[0][5] == 'n' and four[0][0] == "P" and four[2][1] == "u"
)
print("five: {}".format(five.get("fish") == "chips"))
print("five: {}".format(len(five) == 3))
print("six: {}".format(len(six & {2,5,7}) == 2))
print("seven: {}".format(seven == "Wed"))

# -------------------------------------- #
print("\n# -- part 2 -- #")
# Find a value for the `value` variable
# so that all print statements return True.
#value = None
value = [0,1,2,3]
# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# ------------------------------------ #


if type(value) is list:
    print(True)
else:
    print(False)
    
for x in value:
    if not type(x) is int:
        print(False)
    else:
        print(True)

num = 0
while num < value[2]:
    print(True)
    num += 1
    
for y in range(value[3]):
    if y in value:
        print(False)
try:
    value[5] = "Cat"
while True:
    print(False)
except IndexError:
    print(True)
try:
    assert value[3] == -1
except AssertionError:
    print(True)