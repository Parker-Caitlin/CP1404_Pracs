"""
CP1404 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter Sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * 0.15
        print("Bonus: ${:.2f}".format(bonus))
    else:
        bonus = sales / 10
        print("Bonus: ${:.2f}".format(bonus))
    sales = float(input("Enter Sales: $"))
print("Invalid Sales")