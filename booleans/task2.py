#Asking the for the phone number 
phone_number = input("Please enter your phone number:")

#if the phone is 10 digits it  is valid phone number else it is invalid 
if phone_number.isnumeric() and len(phone_number) == 10:
   #isnumeric checks  all the characters are numbers
   print("This is valid number ")
else:
   print("invalid telefonnummer")
   #I put 10digit number and the output was this is valid number 