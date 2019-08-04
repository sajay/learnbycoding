#1.Create an empty dictionary named birthdays
#2. Enter the following data into the dictionary:
#'Luke Skywalker': '5/24/19'
#'Obi-Wan Kenobi': '3/11/57'
#'Darth Vader': '4/1/41'
#3. Write if statements that test to check if 'Yoda' and 'Darth Vader' exist as keys in
#the dictionary, then enter each of them with birthday value 'unknown' if their name does not exist as a key
#4. Display all the key-value pairs in the dictionary, one per line with a space between the name and the birthday, by looping over the #dictionary's keys
#5. Delete 'Darth Vader' from the dictionary
#6. Bonus: Make the same dictionary by using dict() and passing in the initial values when you first create the dictionary

birthdays = {}
birthdays["Luke Skywalker"] = '5/24/19'
birthdays["Obi-Wan Kenobi"] = '3/11/57'
birthdays["Darth Vader"] = '4/1/41'
print(f"Dict : {birthdays}")

for name in["Yoda", "Darth Vader"]:
    if(name in birthdays):
        print(f"{name} already exists")
    else:
        birthdays[name] = 'Unknown'

for value in birthdays:
    print(f"{value}, and date : {birthdays[value]}")

all_keys = birthdays.keys()
print(f"Type of keys : {type(all_keys)}")
print(f"Keys : {all_keys}")

del(birthdays["Darth Vader"])


all_keys = birthdays.keys()
print(f"Keys : {all_keys}")


dupe_birthdays_dict = dict([("Luke Skywalker",'5/24,19'), ("Obi-Wan Kenobi",'3/11/57'), ("Darth Vader",'4/1/41')])
print(dupe_birthdays_dict)
 