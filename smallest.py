n = int(input("enter a number; "))
smallest= 9

while n!=0:
    rem = n % 10
    n = n//10
    if rem<smallest:
        smallest = rem
print(f"The smallest digit is {smallest}")