from guitar import Guitar

def main():

    name = Guitar("Gibson L-5 GES", 1922, 16035.40)
    print(name.name, name.get_age(), name.is_vintage())


main()