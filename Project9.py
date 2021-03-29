# Mikael Hinton
# Project 9
# Functions from https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python

from math import gcd

a = [9720,4158,594,612]
lcm = a[0]

for i in a[1:]:
  lcm = lcm*i//gcd(lcm, i)

print("Least Common Multiple: ",lcm)

print("Greatest Common Factor: ", gcd(*a))