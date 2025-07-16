# this python script acts as a micro-wave
import time
print ("**********************")
print ("cohort 111 MIcro-wave")
print ("**********************")
print("1. open the Micro_wave")
print ("2. put the rice" )
print ("3. set time" )
customes= {}
name=input("enter your name:\n >>>")
time_to_micro_wave = int(input("Duration:\n"))
convert_to_int = float(time_to_micro_wave)
price_to_pay = convert_to_int * 1000
print ("your are charge: #", price_to_pay, "only")
print ("your rice wil be ready in {} min(s) {}" .format(convert_to_int,name))
# seconds = time_to_micro_wave * 60
print ("4. i will let you know when it is ready")
time.sleep(time_to_micro_wave * 60)
print ("5. your food is ready.")
