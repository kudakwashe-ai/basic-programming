a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c):
    print("Conditions met")
else:
    print("Conditions not met")


