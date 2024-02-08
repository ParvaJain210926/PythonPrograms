def check(age, st):
  
    if age >= 21 and passed_exam.upper() == 'Y':
        return "You can enroll in the course."
    else:
        return "You cannot enroll in the course."


age = int(input("Enetr the age "))
st = input("Have you passed your qualifying examination? (Y/N) ")

result = check(age, st)
print(result)
