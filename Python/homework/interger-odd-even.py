print(" *** Interger type and odd even ***")
num = int(input("Enter any number : "))
if num > 0:
    print(num," is positive.")
    if num % 2 == 0:
        print(num," is even.")
    else:
        print(num," is odd.")
elif num % 2 != 0:
    print(num," is negative.")
    if num % 2 == 0:
        print(num," is even.")
    else:
        print(num," is odd.")
else:
    print(num," is zero.")
    print(num," is even.")