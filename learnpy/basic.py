"""This is the basics
of python"""


phrase = "Hello"
print(phrase)

#Script 1

long_string='''This is a very
long string'''

longer_string="""Can also be written
this way"""

print(longer_string)

#Dont want in multiple lines

another_string= "This is a long string \
that will display in 1 line"

print(another_string)

#string concat

new_string=long_string + phrase

#new way to format strings by putting f and {}
print(f"This is a new {long_string} way to print")

#another example
name="Dennis"
num_of_pokemons=6
print(f"{name} has {num_of_pokemons} pokemons. {name} wants {10-num_of_pokemons} more pokemons")
