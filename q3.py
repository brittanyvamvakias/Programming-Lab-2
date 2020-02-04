# File: q3.py
# Author: Brittany Vamvakias
# Date: 01/30/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code takes 5 inputs for 5 subjects and averages the scores. It compares the average with the 4th subject's grade, the 1st subject's grade with the 5th, the 2nd score with the 3rd. Finally, it calculates the needed grade for the 5th subject in order for the average to be 95.

print("*******************Section A*******************")
print()

subject1 = int(input("Enter the subject 1 score: "))
subject2 = int(input("Enter the subject 2 score: "))
subject3 = int(input("Enter the subject 3 score: "))
subject4 = int(input("Enter the subject 4 score: "))
subject5 = int(input("Enter the subject 5 score: "))

average_score = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

print(f"The average score is {average_score}")

print()
print("*******************Section B*******************")
print()

compare_average = average_score >= subject4

print(f"Is the average score greater than or equal to subject4 score? {compare_average}")

print()
print("*******************Section C*******************")
print()

compare_subject1 = subject1 == subject5

print(f"Is subject1 score equal to subject5 score? {compare_subject1}")

print()
print("*******************Section D*******************")
print()

compare_subject2 = subject2 <= subject3

print(f"Is subject2 score less than or equal to subject3 score? {compare_subject2}")

print()
print("*******************Section E*******************")
print()

subject5_new = 475 - subject1 - subject2 - subject3 - subject4

print(f"The score for subject5 should be {subject5_new} to get an average score of 95")

subject5_possible = subject5_new <= 100

print(f"Is it possible to score {subject5_new}? {subject5_possible}")
