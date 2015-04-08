__author__ = 'mike.lyons'

print "Hello World!"
x = raw_input("Enter any number: ")
y = raw_input("Enter another number: ")

try:
    x = float(x)
    y = float(y)
except ValueError:
    x = 0.0
    y = 0.0

print x+y
print x/2
print y**2
