'''
question 1
A  variable  called my_age and set it to  your actual age.
A  variable  called pi and assign it the value 3.14159.
Create a new variable called magic_number that is the result of:
  Your my_age multiplied by 3, then add the  pi, and finally take the modulus (%) with 7.
'''

my_age = 23
pi = float(3.14159)
magic_number = my_age * 3 + pi % 7
print(magic_number)
print("data type",type(magic_number))

'''
q2
Create a variable called secret_word and set it to "PythonIsAmazing".
Print the following using slicing and indexing:
     - The first 6 characters of the string.
     - The last 7 characters using negative indexing.
     - The middle word "Is" using slicing.
     - The string reversed using slicing.
     - Every second character in the string (using step slicing ::2). 
'''

secret_word = "PythonIsAmazing"
print("they first 6 characters are",secret_word[0:6])
#print(secret_word[8])
print("They last 7 characters are ",secret_word[-7:])
print("The middle word", secret_word[6:8])
print("this is The string reversed",secret_word[::5])
print("this are the second character contain in each string", secret_word[::2])

'''
question 3
Using the same secret_word:
   - Convert only the first word ("Python") to uppercase and print it.
   - Convert the rest of the string ("IsAmazing") to lowercase and print it.
   - Combine the uppercase and lowercase parts into one new string and print it.
'''
secret_word = "PythonIsAmazing"
first_char = (secret_word[0:6]).upper()
print(first_char)
rest_char = (secret_word[6:]).lower()
print(rest_char) 
combine = (f"{first_char}{rest_char}")
print(combine)
