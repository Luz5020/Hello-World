def addition():
    number1 = input("Enter first Number:\n")
    number2 = input("Enter second Number:\n")
    number1 = float(number1)
    number2 = float(number2)
    # When integrating, turn these into return statements
    print(number1 + number2)


def division():
    dividend = input("Enter dividend:\n")
    divisor = input("Enter divisor:\n")
    dividend = float(dividend)
    divisor = float(divisor)
    # When integrating, turn these into return statements
    print(dividend / divisor)


def iseven():
    number = input("Enter number now:\n")
    number = float(number)
    x = number % 2
    if x == 0:
        # When integrating, turn these into return statements
        print("number is even")
    else:
        # When integrating, turn these into return statements
        print("number is not even")


def multiplication():
    factor1 = input("Enter first Factor:\n")
    factor2 = input("Enter second Factor:\n")
    factor1 = float(factor1)
    factor2 = float(factor2)
    # When integrating, turn these into return statements
    print(factor1 * factor2)


def subtraction():
    number1 = input("Enter first Number:\n")
    number2 = input("Enter second Number:\n")
    number1 = float(number1)
    number2 = float(number2)
    print(number1 - number2)
