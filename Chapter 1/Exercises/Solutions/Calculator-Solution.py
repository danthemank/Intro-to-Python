# Calculator Program
# Include the following math computations, defined as functions and taking user input for values and what computation to execute.
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division with result in decimal format
# 6. Division with result in fraction format
# 7. Exponential

#define all functions
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divisionDecimal(x, y):
    return x / y

def divisionFraction (x, y):
    return str(int(x / y)) + " Remainder " + str(x % y)

def exponential(x, y):
    return x ** y


#Program start
uinput = ""

print("Welcome to the calculator program.")

while(uinput != "q"):
    print("Which computation would you like to make?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division with Decimals")
    print("5. Division with Fraction Output")
    print("6. Exponential")
    print("Enter 'q' to exit.")

    uinput = raw_input("Choice: ")

    if(uinput == "q"):
        break;

    uinputx = input("First Number: ")
    uinputy = input("Second Number: ")

    if(uinput == "2"):
        print subtraction(uinputx, uinputy)

    elif(uinput == "3"):
        print multiplication(uinputx, uinputy)

    elif(uinput == "4"):
        print divisionDecimal(uinputx, uinputy)

    elif(uinput == "5"):
        print divisionFraction(uinputx, uinputy)

    elif(uinput == "6"):
        print exponential(uinputx, uinputy)

    else:
        print addition(uinputx, uinputy)