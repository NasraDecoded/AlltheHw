#create an empty list
pairs = []

#start a loop that starts at 1 and stops at 10

for i in range(1, 11):
    j = i ** 2        # square of i
    pair = (i, j)     # create the tuple
    pairs.append(pair) #add

print(pairs)