# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:55:03 2025

@author: HP
"""

#Python Variables
distance_travelled_mi = 100

time_taken_min = 1200

time_taken_hr = time_taken_min/60

print("Number of miles traveled", distance_travelled_mi)
print("Number of hours traveled", time_taken_hr)
print("Speed in mph", distance_travelled_mi/time_taken_hr)

print()

#test
#print("Time taken in minutes", Time_Taken_Min)
# Answer: Will not work
#Correct syntax
print("Time taken in minutes", time_taken_min)

#_total_memory = 0 should be as below without indentation
 
_total_memory = 0
print("Total memory:", _total_memory)
#_total% =25 should not use % symbol, Variable names are a combination of letters, numbers and underscores alone; not other symbols or reserved words. Also variable names cannot start with a number,,they can only start with a letter or an underscore(with no indentation)

#this variable is correct
totalPercentage =10

#1stPass =3  should be and not start with a  number:
firstPass = 3

myName = "Faith Adhiambo"
print(myName)

#should not use reserved words
#class = "CIS 415"  You could say:
myclass = "CIS 415"
print("My name is", myName, "and my class is", myclass)


fruits = "Apples and Oranges"
numApples=10
numOranges=20
print("I have", fruits, "...I have", numApples, "Apples", numOranges, "Oranges")