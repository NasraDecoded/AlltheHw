#Asking the user to put a sentence there
sentence = input("what is your sentence? ")
#Separating the sentence everytime it sees a space
words = sentence.split()
#create a dictionary 
word_count = {}

for word in words:
    word_count[word] = 0
#count the no times the word is seen in the sentence
for word in words:
    current_value = word_count.get(word)
    word_count[word] = current_value + 1
#print the result afterward
print(word_count)


