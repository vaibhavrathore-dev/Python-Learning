digits = int(input("Enter a number: "))
digit = 0

while digits!=0:
    rem = digits % 10
    digits = digits//10
    digit = digit + rem
print(f"The addition is {digit}")