STRING_TO_PRINT = "Hello World"
for i in range(0, 5):
    print(STRING_TO_PRINT)

print(list(range(3)))
print(list(range(17, 2, -3)))

names = ["Hanan", "Tom", "Zack", "Aharon"]
# loop - type 1
for name in names:
    if name == "Zack":
        break
    if name == "Tom":
        continue
    else:
        pass
    print(name)

# loop - type 2
for i in range(len(names)):
    print(names[i])

for name in names:
    name = "dotan"

for i in range(len(names)):
    names[i] = "dotan"

# loop - type 3
a = 0
while a < 5:
    print(a)
    a = a + 1

