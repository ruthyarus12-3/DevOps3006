import requests

print("ruth")
try:
    response = requests.get("jfkdsl://github.com")
except Exception as e:
    print("something went wrong")
    print(e.args)
print("reuven")

try:
    f = int(input("enter number: "))
    r = 5 / 0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("something went wrong")
    print(e.args)
