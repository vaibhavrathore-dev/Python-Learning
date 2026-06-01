digit = int(input("Enter a number: "))
reverse = 0


while digit!= 0:
     rem= digit%10
     digit= digit//10
     reverse = reverse*10 + rem
print(f"the result is {reverse}")

        
        