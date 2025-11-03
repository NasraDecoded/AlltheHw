import random 

#Create 2 lists and a common one 

list1 = []
list2 = []
common = []

#Fill in list 1
count1 = 0
while count1 < 10:
    list1.append(random.randint(1,10))
    count1 +=1

#Fill in list 2
count2 = 0
while count2 < 10:
    list2.append(random.randint(1,10))
    count2 +=1

check = 0
while check < 10:
    number = list1 [check]
    if number in list2 and number not in common:
       common.append(number)
    check +=1
print("List 1 is:",list1)
print("List 2 is:",list2)
print("The Common is:",common)