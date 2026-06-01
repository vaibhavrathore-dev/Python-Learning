n = int(input("Enter a Number: "))
arm = 0
original = n

while n>0:
    rem = n%10
    n = n//10
    arm = arm + pow(rem,3)
if arm ==original:
    print(f"{arm} is armstrong number")
else:
    print(f"{original} is not  armstrog number")
    
