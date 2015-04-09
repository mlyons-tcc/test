__author__ = 'mike.lyons'
print "test v1.0.4"
print "Hello Customer!"

while True:
    x = raw_input("Enter any number: ")
    y = raw_input("Enter another number: ")

    try:
        x = float(x)    # use float so that division works
    except ValueError:
        x = 0.0
    try:
        y = float(y)
    except ValueError:
        y = 0.0

    print "Sum: " + str(x+y)
    print "Difference: " + str(x-y)
    print "Product: " + str(x*y)
    print "Quotient: " + (str(x/y) if y != 0.0 else str(0.0))
    print "Square of 1st number: " + str(x**2)
    print "Square Root of 2nd number: " + str(y**.5)

    user_exit = raw_input("Exit? (y/n): ")
    if user_exit == 'y' or user_exit == 'Y':
        break
print "Goodbye Customer!"
