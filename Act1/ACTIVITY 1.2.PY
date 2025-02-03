num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    highest = num1
    if num2 >= num3:
        middle = num2
        lowest = num3
    else: 
        middle = num3
        lowest = num2
elif num2 >= num1 and num2 >= num3:
    highest = num2
    if num1 >= num3:
        middle = num1
        lowest = num3
    else: 
        middle = num3
        lowest = num1
else:
    highest = num3
    if num1 >= num2:
        middle = num1
        lowest = num2
    else:
        middle = num2
        lowest = num1

print("Numbers in descending order: ", highest, middle, lowest)
