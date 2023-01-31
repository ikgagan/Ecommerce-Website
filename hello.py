import sys



a=0
for i in range(5):
    if i % 2 == 0:
        a +=1
    if a % 2 == 0:
        a -=1

    print(f"a is {a}")

