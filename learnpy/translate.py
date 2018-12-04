
#Write a script translate.py that asks the user for some input with the following prompt:
#Enter some text:
#You should then use the replace() method to convert the text entered by the user into
#"leetspeak" by making the following changes to lower-case letters:
#The letter: a becomes: 4
#The letter: b becomes: 8
#The letter: e becomes: 3
#The letter: l becomes: 1
#The letter: o becomes: 0
#The letter: s becomes: 5
#The letter: t becomes: 7

user_input = input("Enter a string")
print(f"user entered : {user_input}")

replaced_input = user_input.replace("a", "4")
replaced_input = replaced_input.replace("b", "8")
replaced_input = replaced_input.replace("e", "3")
replaced_input = replaced_input.replace("l", "1")
replaced_input = replaced_input.replace("o", "0")
replaced_input = replaced_input.replace("s", "5")
replaced_input = replaced_input.replace("t", "7")

print(f"Replaced string is : {replaced_input} ")




