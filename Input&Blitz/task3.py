import random

#Ask the user for the input 

word=input ("Enter a word please: ")

#Repeat it 5times to make 5random combination 
for i in range(5):
    random_word= ''.join(random.sample(word,len (word)))
    print(random_word)

    #result after i put hello olelh
#hoell
#lhoel
#leolh
#ehllo