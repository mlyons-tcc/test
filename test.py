__author__ = 'mike.lyons'

print "Hello World!"

while True:
    x = raw_input("Enter any number: ")
    y = raw_input("Enter another number: ")

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        x = 0
        y = 0

    print "Sum: " + str(x+y)
    print "Product: " + str(x*y)
    print "Square of 2nd number: " + str(y**2)

    user_exit = raw_input("Exit? (y/n): ")
    if user_exit == 'y' or user_exit == 'Y':
        break
print "Goodbye World!"
