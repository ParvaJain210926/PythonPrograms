def check(age, income):

    if age >= 18 and income >= 15000:
        print("You are eligible")
    
    else:
        print("You are not eligible")

age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))

check(age,income)
