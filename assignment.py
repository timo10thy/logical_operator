print ("user details")

name=input("what is your name \n>>>")
print(type(name))
age=int(input("Are old are you \n>>>"))
print(type(age))
Height=float(input("what is your height \n>>>"))
print(type(Height))
hobbies=input("Your hobbies \n")
print(type(hobbies))

is_married = input("Are you married? (yes/no):\n ").lower()

married = True if is_married == "yes" else False

print(type(married))
print(f"your details are: {name}, {age}, {Height},{hobbies},{married}")
