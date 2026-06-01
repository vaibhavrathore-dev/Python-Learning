weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight/pow(height,2)

if bmi<18.5:
    print("You are underweight")
elif bmi>18.5 and bmi<24.9:
    print("You ar healthy")
elif bmi>25.0 and bmi<29.9:
    print("You are overweight")
else:
    print("You are obeese")