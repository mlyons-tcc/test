__author__ = 'mike.lyons'

print "Hello World!"
x = raw_input("Enter any number: ")
y = raw_input("Enter another number: ")

try:
    x = int(x)
    y = int(y)
except ValueError:
    x = 0
    y = 0

print x+y
print x/2
print y**2
