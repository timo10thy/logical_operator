print ("welcome to dish-cafe")
name=input('what is your name\n')


print ("welcome to dish-cafe {}".format(name))
print ("what do you want to order")
order = input("order\n")
print ("plate of food cost 1000")
quantity=int(input("how many plates\n"))
amount =quantity * 1000
print("total price for require orders is {}".format(amount))
import time
print ("how long do you want it to be micro wave")
duration = float(input("duration for it to be micro wave \n >>>"))
#time.sleep(duration * 60)
print (f"your {order} will be ready in {duration}") 
time.sleep(duration * 60)
print("your order is ready")
print("thank you for your patronage see you next time")

