user_input = input("enter something nice: ")

#Finding the number of lower case characters based on using a count of the lower function
count = 0

for i in user_input:
    if(i.islower()):
        count = count + 1

print("The number of lower case characters is: ")
print(count)

#Finding the number of upper case characters based on using a count of the upper function
upcount = 0

for j in user_input:
    if(j.isupper()):
        upcount = upcount + 1

print("the number of upper case characters is:")
print(upcount)

#How to count the special characters in a sentence
specials = ['!', ',', " \ ", ";", " \ ", ".", "-", "?"]
special_count = 0

for k in user_input:
    if user_input in specials:
        special_count = special_count + 1

print("The number of special characters is:")
print(special_count)

print("Therefore the total number of characters is ", count + upcount + special_count)

Dict = {"Upper case" : upcount, "lower case" : count, "Special characters" : special_count}
Print(Dict)