# File: q4.py
# Author: Brittany Vamvakias
# Date: 01/30/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code take three inputs for three cat's weight, and calculates the mean weight, the variance of the weights, and the standard deviation of the weights.

print("*******************Section A*******************")
print()

cat1 = int(input("Enter the weight of cat1: "))
cat2 = int(input("Enter the weight of cat2: "))
cat3 = int(input("Enter the weight of cat3: "))

print(f"The weight of cat1 is: {cat1} lbs")
print(f"The weight of cat2 is: {cat2} lbs")
print(f"The weight of cat3 is: {cat3} lbs")

print()
print("*******************Section B*******************")
print()

mean_weight = (cat1 + cat2 + cat3) / 3

print(f"The mean weight is: {mean_weight} lbs")

print()
print("*******************Section C*******************")
print()

variance_weights = ((cat1 - mean_weight)**2 + (cat2 - mean_weight)**2 + (cat3 - mean_weight)**2) / 3

print(f"The variance of the weights is: {variance_weights} lbs^2")

print()
print("*******************Section D*******************")
print()

sd_weights = variance_weights**0.5

print(f"The standard deviation is: {sd_weights} lbs")

