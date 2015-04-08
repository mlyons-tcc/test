__author__ = 'mike.lyons'

print "Hello World!"

while True:
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

    user_exit = raw_input("Exit? (y/n): ")
    if user_exit == 'y' or user_exit == 'Y':
        break
print "Goodbye World!"
