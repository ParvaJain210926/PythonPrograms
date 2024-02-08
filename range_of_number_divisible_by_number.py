def display(start, end, div):
    for num in range(start, end + 1):
        if num % div == 0:
            print(num, end=" ")

start= int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
div = int(input("Enter the divisor: "))
display(start, end, div)
