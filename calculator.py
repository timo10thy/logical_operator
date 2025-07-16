# A simple calculator app
print('''          1.Addition
	  2.Subtraction
	  3.Multiplication
	  4.Division
'''
)
print("Enter two numbers to add")
first_number= input("first number\n>>>")
second_number = input("second number\n>>>")
sum =float( first_number) + float(second_number)
print(f"{first_number } + {second_number} = {sum:.2f}")
print("****************************")
print("Subtraction")
print("Enter two numbers to subtract")
first_number = input("first number\n>>>")
second_number = input("second number\n>>>")
sub =float( first_number) - float(second_number)
print(f"{first_number } - {second_number} = {sub:.2f}")
print("*********")
print("Enter two numbers to multiply")
first_number= input("first number\n>>>")
second_number = input("second number\n>>>")
multiply =float( first_number) * float(second_number)
print(f"{first_number } * {second_number} = {multiply:.2f}")
print("*********")
print("Enter two numbers for division")
first_number= input("first number\n>>>")
second_number = input("second number\n>>>")
division =float( first_number) / float(second_number)
print(f"{first_number } / {second_number} = {division:.2f}")
print("*********")
print("Enter two numbers for expon")
first_number= input("first number\n>>>")
second_number = input("second number\n>>>")
expon =float( first_number) ** float(second_number)
print(f"{first_number } ** {second_number} = {expon:.2f}")


