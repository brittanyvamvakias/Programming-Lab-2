# File: extra_credit.py
# Author: Brittany Vamvakias
# Date: 01/30/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description:

print("*******************Section A*******************")
print()

string_one = input("Enter the first input: ")
string_two = input("Enter the second input: ")

print(f"Is the length of string_one equal to 5? {len(string_one) == 5}")

print(f"Is the length of string_two equal to 7? {len(string_one) == 7}")

print()
print("*******************Section B*******************")
print()

numbers_one = string_one[1::2]
letters_one = string_one[0::2]

print(f"letters_one is: {letters_one}")
print(f"numbers_one is: {numbers_one}")

print()
print("*******************Section C*******************")
print()

numbers_two = string_two[0::2]
letters_two = string_two[1::2]

print(f"letters_two is: {letters_two}")
print(f"numbers_two is: {numbers_two}")

print()
print("*******************Section D*******************")
print()

quotient1 = int(numbers_two) // int(numbers_one)
remainder1 = int(numbers_two) % int(numbers_one)

print(f"The quotient is: {quotient1} and the remained is: {remainder1}")

print()
print("*******************Section E*******************")
print()

result1 = letters_two + letters_one

print(f"The result of concatenating letters_two with letters_one: {result1}")
