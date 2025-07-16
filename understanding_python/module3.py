weather = "good"
if weather == "good":
	print("go for a walk")
else:
	print("sleep")

number1 = int(input("enter the first number\n>>>"))
number2 = int(input("enter the second number\n>>>"))
if number1 > number2:
	larger_number = number1
else:
	larger_number = number2
print("the larger number",larger_number)

num1 = int(input("enter the first number\n>>>"))
num2 = int(input("enter the second number\n>>>"))
if num1 > num2:larger_num = num1
else:larger_num = num2
print(larger_num)

largest_number = -999999999
number = int(input())
if number == -1:
	print(largest_number)
	exit()
if number> largest_number:
	largest_number = number

one= int(input("enter number\n>>>"))
two = int(input("enter number\n>>>"))
three = int(input("enter number\n>>>"))
largest_number = max(one,two,three)
print("your largest number is ", largest_number)
