def fun(num):
    temp= 0
    while num> 0:
        temp += num % 10
        num //= 10
    return temp

num = int(input("Enter a number: "))
print("Sum of digits:", fun(num))
