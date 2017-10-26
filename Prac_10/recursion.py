"""
CP1404 Prac
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        return
    print(n ** 2)
    return do_something(n - 1)
do_something(4)

def count_blocks(n):
    if n <= 0:
        return 0
    return n + count_blocks(n - 1)


def build_pyramid():
    user_input = int(input("Input the number of rows "))
    print('your pyramid is this many blocks', count_blocks(user_input))

build_pyramid()