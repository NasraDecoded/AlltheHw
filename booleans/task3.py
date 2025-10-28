#variable with my name stored in lowercase
my_name = "nasra"

#input of the name of the user
user_input = input("Please,enter your name!,Thank you")

#Compare if the stored and the input are the same even and always convert to lower
if user_input.lower().strip() == my_name: #i got an error untill i noticed i didnt put :
   print(True)
else:
   print(False) 

   #true and false didnt work untill it was in capital 
   #When i input my name in first it print out true untill i put 
   # someone else name and put again my name then it return false ....


  