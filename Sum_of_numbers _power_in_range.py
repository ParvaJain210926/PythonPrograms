num=int(input("enter the number"))
def compute(n):
    temp=1
    for i in range(1,n):
        temp=temp*n
    print("yout total value :",temp)
compute(num)
