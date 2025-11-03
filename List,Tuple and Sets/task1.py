import random 

count = 0
biggest = 0

while count < 10:
    number = random.randint(1,100)
    print("The number is :", number)

    if number > biggest:
    
       biggest = number 

    count= count+1

print("Biggest number is ", biggest)

