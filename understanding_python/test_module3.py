'''
text = input("your text\n")
if text == text.upper():
	print("spathiphyllum is the best plant ever!")
else:
	print("No, i want a big spathiphyllum")

income = float(input("Enter your income\n"))
if income <= 85528:
	tax = (income * 0.18) - 556.02
else:
	tax = 14839.02 + (income -85528) * 0.32
tax = round(tax, 0)
print(tax,'halers')

x = 5
y = 10
z = 8
print(x>y)
print(y>z)

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

secret_number = 777

print("Guess the secret number to escape the loop!")

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")

i = 100
while i >=1:
	print(i,"counting")
	i -= 1

for i in range(10):
	print("the current value of i",i)
print("******************")
for i in range(2,8):
	print ("the current value of i",i)
print("********************")
for i in range(3,9):
	print("the current value of i",i)
print("***********************")
for i in range(2,8,3):
	print("the current value of i",i)
print("*******************")
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
print("****************")
import time
for i in range(1,6):
	time.sleep(1)
	print(i, "Mississippi")
time.sleep(1)
print("Ready or not, here I come!")

print("******************")
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

    print("stuck in a loop")

print("*********************")
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)


for i in range (0,11):
    if i % 2 != 0:
     print(i)
print("******************")
for i in range(2,12):
    if i % 2 == 0:
     print(i)
'''

x = 1
while x <11:
    if x % 2 != 0:
     print(x)

