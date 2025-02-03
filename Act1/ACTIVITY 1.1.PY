num1 = float (input("Enter First Number: "))
num2 = float (input("Enter Second Number: "))
num3 = float (input("Enter Third Number: "))

if num1 > num2:
    if num1 > num3:
        highest = num1
    else:
        highest = num3
else:
        if num2 > num3:
            highest = num2
        else:
            highest = num3

print (f"The highest number is:", highest)