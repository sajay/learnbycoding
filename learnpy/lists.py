#Create a list named desserts that holds the two string values "ice cream" and "cookies"
#2. Sort desserts in alphabetical order, then display the contents of the list
#3. Display the index number of "ice cream" in the desserts list
#4. Copy the contents of the desserts list into a new list object named food
#5. Add the strings "broccoli" and "turnips" to the food list
#6. Display the contents of both lists to make sure that "broccoli" and "turnips" haven't been added to desserts
#7. Remove "cookies" from the food list
#8. Display the first two items in the food list by specifying an index range
#9. Create a list named breakfast that holds three strings, each with the value of "cookies", by splitting up the string "cookies, cookies, cookies"
#10. Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64] , as the argument and then outputs only the numbers from the list that fall between 1 and 20 (inclusive)

deserts = []
deserts.extend(["ice cream", "cookies"])

deserts.sort()
print(f"Sorted deserts : {deserts}")

index_ic = deserts.index("ice cream")
print(f"Index of ice cream : {index_ic}")

food = []
food.extend(deserts)

#food = deserts[:] This copies list contents into food as well

food.append("brocolli")
food.append("turnips")

print(f"Food list contents : {food}")

food.remove("cookies")

print(f"Food list 2 items : {food[:2]}")

cookie_string = "cookies, cookies, cookies" 
breakfast = cookie_string.split(", ")

def printselectvals(num_list):
    for n in range(0, len(num_list)):
        if (num_list[n] < 20):
            print(f"Value is {num_list[n]}")
            
numbers = [2, 4, 8, 16, 32, 64]
printselectvals(numbers)
        