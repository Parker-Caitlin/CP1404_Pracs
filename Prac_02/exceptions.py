"""
CP1404 - Prac
Answer the following questions:
1. When will a ValueError occur? If there is a decimal point in either numerator or denominator
2. When will a ZeroDivisionError occur? when you input a 0 in te denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError? no because you can't divide anything by 0.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")