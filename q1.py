# File: q1.py
# Author: Brittany Vamvakias
# Date: 01/30/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: Section A of this code takes an input of a four digit number, reverses the number and prints the reversed number. Section B takes a seperate input for a first and last name and creates a string for the full name and prints the length of the full_name variable.

print("*******************Section A*******************")
print()

number1 = int(input("Enter the four digit number: "))

thousands = number1 // 1000
hundreds = (number1 % 1000) // 100
tens = (number1 % 100) // 10
ones = (number1 % 10)
number1_reversed = ones * 1000 + tens * 100 + hundreds * 10 + thousands * 1

print(f"The reverse of {number1} is {number1_reversed} and it's type is <class 'int'>")

print()
print("*******************Section B*******************")
print()

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
full_name = first_name + " " + last_name

print(f"The full name of the student is {full_name}, and the length of the variable full_name is {len(full_name)}.")


