def check(num):
    if num > 0:
        print(num,"is positive")
    elif num < 0:
        print(num,"is negative")
    else:
        print(num,"is zero")

num = float(input("Enter a number: "))
check(num)
