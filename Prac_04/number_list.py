"""
CP1404 Prac
"""
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("The First number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The avaerage number is {}".format(sum(numbers)/5))