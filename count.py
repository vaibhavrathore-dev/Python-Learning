n =  int(input("Enter a  number : "))
count = 0

if n==0:
    print("Invalid input")

else:
    while n!=0:
        n =n//10
        count = count+1
print(f"The no. of digits are {count}")