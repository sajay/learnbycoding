#Create a tuple named cardinal_nums that holds the strings "first", "second" and "third" in order
#2. Display the string at position 2 in cardinal_nums by using an index number
#3. Copy the tuple values into three new strings named pos1 , pos2 and pos3 in a single line of code by using tuple unpacking, then print those string values

cardinal_nums =("first", "second", "third")
index_of_third = cardinal_nums.index("third")
print(f"Position 2 : {cardinal_nums[1]}, {index_of_third}")
pos1, pos2, pos3 = cardinal_nums
print(f"{pos1}, {pos2}, {pos3}")