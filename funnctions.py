def reverse(n):
    original = n
    reverse = 0
    while n>0:
        rem = n  % 10
        n = n // 10
        reverse = reverse * 10 +  rem

    if original == reverse:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
    


a = int(input("Enter any Number: "))
reverse(a)
