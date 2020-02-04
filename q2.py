# File: q2.py
# Author: Brittany Vamvakias
# Date: 01/30/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code takes a string input from the user, prints the length of the input, and converts the string to all upper-case. It then takes the upper-case string, creates and prints a palindrome and checks if the created string is actually a palindrome. The length of the palindrome is checked to see if its double the length of the original string and prints the result.

print("*******************Section A*******************")
print()

user_input = input("Enter the input string: ")
print(f"The length of the input string is {len(user_input)}")

print()
print("*******************Section B*******************")
print()

result1 = user_input.upper()
print(f"The input string with chracters converted to upper case is {result1}")

print()
print("*******************Section C*******************")
print()

palindrome1 = result1 + result1[::-1]
print(f"The palindrome is {palindrome1}")
check_palindrome = palindrome1 == result1 + result1[::-1]
print(f"The comparison result is {check_palindrome}")

print()
print("*******************Section D*******************")
print()

result2 = len(palindrome1) == len(result1) * 2
print(f"The variable result2 is {result2}")
