#String variable where the user put the variable
text= input("Enter a String: ")

#see if the string length is less than 2,return an empty string 
if len (text) < 2:
        answer= ""
else:
    #else using string slicing technique first two characters and last two characters if greater than 2
    answer = text[:2] + text [-2:]
#Put the words helloword,my,x and expected should be held,mymymempty
print(answer)

#answer held,mymy

