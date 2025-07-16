'''
bio = "programmer"
print(len (bio))
print(bio[6])
details = "python programmer to the core"
print(len(details))
print(details[0:7].upper())
print(details[7:18].lower())
print(details[18:21].upper())
print(details[21:25].lower())
print(details[25:].upper())
text = 'geeKs For geEkS'
print("\nConverted String:")
print(text.upper())
print(text.capitalize())
print(text[-5::1])
print("step 2 ",text[-5::2])
print("step 3", text[-5::3])
print(text[-5:-1:1])
print('all the string',text [::])
print('all the string',text [:])
print("all the string",text [0:])
print("^^^^^^^^^^^^^^^^^^^^^")
s = "abcdefghi"
print(s[::1])
count = "how many tribes ifbt sidt teeeth"
print(count.count("t"))
string = "Python is awesome, isn't it?"
substring= "i"
count = string.count(substring,8,25)
print(count)


word = "good"	
new_word = len(word) // 2
fw_word = word[:new_word]
sew_word = word[new_word:]
print(fw_word)
print(sew_word)

one = 5
two= 2
result = one // two
print(result)
print(float(result))


new_num = float(6)
old_num = float(2)
print(new_num//old_num)

words = "blockfuse labs"
print("lenght of blocfuse labs",len(words))
new_words = len(words) // 2
print(" lenght for new word",new_words)
div_first = words[:new_words]
print(div_first)
div_sec= words[new_words:]
print(div_sec)


tech_words = "java"
tech_lan = len(tech_words) //2
first_lan = tech_words[:tech_lan]
print(first_lan)
second_lan = tech_words[tech_lan:]
print(second_lan)


block = "cohort"
labs = len(block) // 2
la = block[:labs]
bs =block [labs:]
print(la, bs)


health = "drugs"
med = len(health)//2
new_med = health[:med]
new_h = health[med:]
print("using .format method {} {}".format(new_med ,new_h))

users= "user@domain.com"
new_users = users[0:5]
print(new_users)
mail="gmail"
user_gmail = ("{}{}".format(new_users , mail))
print(user_gmail)
'''
fruit = "Mango, orange, kiwi"
list_fruit = fruit.split(",")
print(list_fruit)
start_fruit = fruit
print(start_fruit.lower().startswith('Mango'))
print(not "Mango" in fruit.lower())

record = "james Abuja 150000.5 NG0921"
split_record = record.split()
print(split_record)
print("index position",split_record[2])
index_two =float( split_record[2])
print(f"this is index_two {index_two:,.2f}")

var = 0
print("this is the value of var", var == 0)
#black_sheep == (black_sheep*white_sheep)
#print(black_sheep)
print("whitesheep" > "blacksheep")
fifty = 55
print("yes",fifty == 55)
print("no", fifty == 5)

