n = int(input("Enter a number: "))
product = 1

while n!=0:
    rem = n % 10
    n = n // 10
    product = product * rem
print(f"The  product of every digit is {product}")