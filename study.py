import time
print ("step to boil rice")
print ("first step: after putting your gas on ")
print ("put your pot containing a water on it")
print ("to boil")
print ("how long do you want it boil")
heating_water = float(input("duration to boil: \n"))
print ("your water will be ready in {}".format( heating_water))
time.sleep(heating_water * 60)
print ("your water is ready")
print (" put in your rice") 

