#Write a script temperature.py that includes two functions. One function takes a Celsius
#temperature as its input, converts that number into the equivalent Fahrenheit
#temperature and returns that value. The second function takes a Fahrenheit temperature
#and returns the equivalent Celsius temperature. Test your functions by passing input
#values to them and printing the output results.
#For testing your functions, example output should look like:
#72 degrees F = 22.2222222222 degrees C
#37 degrees C = 98.6 degrees F
#In case you didn't want to spend a minute searching the web or doing algebra (the
#horror!), the relevant conversion formulas are:
#1. F = C * 9/5 + 32
#2. C = (F - 32) * 5/9

def celcius_to_farenheit(celcius_temp):
    farenheit_temp = float(celcius_temp) * 9/5 + 32.0
    return farenheit_temp

def farenheit_to_celcius(farenheit_temp):
    celcius_temp = (float(farenheit_temp) - 32.0) * 5/9
    return celcius_temp

celcius_temperature = input("Enter temp in celcius :")
print(f"Celcius temp entered : {celcius_temperature} and in farenheit is {celcius_to_farenheit(celcius_temperature)}")

far_temperature = input("Enter temp in farenheit :")
print(f"Farenheit temp entered : {far_temperature} and in celcius is {farenheit_to_celcius(far_temperature)}")
