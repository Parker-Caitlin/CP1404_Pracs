"""
Prac 3- CP1404
Caitlin Parker
"""
def main():
    user_name = get_name()
    print(user_name[1::2])


def get_name():
    user_name = input("Enter Name: ")
    check_len = len(user_name)
    while check_len <= 0:
        user_name = input("Error. Input Name: ")
        check_len = len(user_name)
    return user_name


main()