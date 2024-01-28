# 3rd Python Program

num = int(input("Enter the number: "))
number = []

for i in range(num):
    num2 = float(input("Enter number ! " + str(i + 1) + " == "))
    number.append(num2)

total = sum(number)
print("the list u entered !=!",number)
print("Sum of the", num, "numbers is:", total)
