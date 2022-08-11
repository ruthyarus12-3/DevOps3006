is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

print(type(a == b))
if a < b and strOne == "Ruth" or strThree == "Three":
    print("a is smaller than b")
elif a < b and (b != 1 or not strThree == "Three"):
    print("boo")
elif a == b:
    print("a equals b")
else:
    print("something")

names = ["Hanan", "Tom", "Zack", "Aharon"]
name_to_find = "Ariel"
other_list = ["1"]
if name_to_find in names:
    print(f"we found {name_to_find}")

if other_list:
    print("other list has values")

if len(other_list) > 0:
    print("boo")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if type(k) is int:
    print("integer")
elif type(k) is str:
    print("string")

print(k == f)
print(k is f)
print(t == e)
print(t is e)

