# 7 boom game
x_boom = 7
for i in range(1, 100):
    if i % x_boom == 0 or str(x_boom) in str(i):
        continue
    print(i)

# This else will be performed if the for loop didn't break
for i in range(1, 100):
    if i % x_boom != 0 and not str(x_boom) in str(i):
        continue
    print(i)
else:
    print("loop finished successfully")

a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("blabla")
