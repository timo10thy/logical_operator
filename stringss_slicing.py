'''
quote = "five slice of bread"
print(len(quote))
print(quote[0:1])
print(quote[1:2])
print(quote[2:3])
print(quote[3:4])
print(quote[4:5])
print(quote[5:6])
print(quote[6:7])
print(quote[7:8])
print(quote[9:10])
print(quote[10:11])
print(quote[11:12])
print(quote[12:13])
print(quote[13:14])
print(quote[14:15])
print(quote[15:16])
print(quote[16:17])
print(quote[17:18])
print(quote[18:19])
print(quote[19:])


'''
chain ="blockchain"
number = 50
total = 1 
totals = total + number + len(chain)
print(totals)


tech = "blockchain"
print (tech[-10:-7])

chain = "blockchain"
print(chain.upper())
'''

pros = "programmer"
pro = (pros[-10:-7])
print(pro)
print(pro.upper())
print(pro.lower())

grammer = (pros[-7:])
print(grammer)
print(grammer.upper())
print(grammer.lower())

 
first_namess = "python"
print(first_namess.capitalize())
#print(first_namess[0].upper() + first_namess [1:])
#print("string slicing", first_namess[0:1].upper())
#print(first_namess[0].upper()+ first_Namess[1:7])

PI = 3.1415

print("PI:{:.2f}".format(PI))

height = 45
print(f"My height is {height:.2f}")
acc_bal= 5000
print(f"your account balance is  ₦{acc_bal:.2f}")

bio = "my name is Tom"
print(not "name" in bio)
#print(bio in not "name")
#print('\a')
fruits = "Apple, Mango, Orange,Banana,kiwi"
list_fruits = fruits.split(",")
print(list_fruits)
'''
'''
record = "james Abuja 150000.5 NG0921"
#print(bio in not "name")

print ("Salary Slip")
print("------------")
name_of_james = record[0:5]
print("Name:\t",name_of_james.capitalize())

initials =  name_of_james[0:1]
print(initials)
print ("Initial:\t",initials.capitalize())
id = record[-6:]
print("ID:\t",id)
valid = "yes"
print("Valid ID:\t",valid)
Monthly = float(record[12:20])

print(f"Monthly Salary\t: {Monthly:,.2f}")
'''
message ="GhostNet#X44CR#98.654#TRC8821"
print('ALERT REPORT')
print("------------------------")
code_name = message[0:8]
#print(code_name)
print("Code Name:\t", code_name)
message_code = message[9:14]
print("Message Code:\t",message_code)
last = message[-6:-5]
print("Last Letter:\t",last)
trace_id = message[-7:]
print("Trace Id:\t", trace_id) 
trace = "Yes"
print("Traceable:\t",trace)
severity = message[15:20]
print("Severity Level:\t",severity)

