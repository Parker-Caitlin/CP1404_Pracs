"""
CP1404 - Practical
Pseudocode for temperature conversion
help me

"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()


    def calc_celsius():
        global celsius, fahrenheit
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32


    def calc_fanhrenheit():
        global celsius
        fanhrenheit = float(input("Fanhrenheit: "))
        celsius = 5 / 9 * (fanhrenheit - 32)


    while choice != "Q":
        if choice == "C":
            calc_celsius()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            calc_fanhrenheit()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()
