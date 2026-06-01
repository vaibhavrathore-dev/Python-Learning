n = int(input("Enter a number: "))
largest = 0

while n!=0:
    rem = n%10
    n = n//10
    if rem>largest:
        largest =  rem

print(f"The largest umber is {largest}")