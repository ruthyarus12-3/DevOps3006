def print_hello(name, excluded_name, hello_word):
    if name != excluded_name:
        print(f"{hello_word} {name}")


print_hello("Boo", "foo", "koo")

c = 3


def mult(x, y, c):
    from utils import c
    result1 = x * y + c
    result2 = x / y
    return result1, result2


r = mult(10, 4, 2)
a, b = mult(10, 4, 2)
print(r[0])
print(r[1])

user_name = input("enter your name: ")
print(f"boo{user_name}")
