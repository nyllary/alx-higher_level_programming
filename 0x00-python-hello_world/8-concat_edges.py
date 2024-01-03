#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntan"
str = str[39:66] + ' ' + str[106:-18] + ' ' + str[0:-122]
print(str)
