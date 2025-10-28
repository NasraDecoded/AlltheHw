import random #box of suprise numbers

#Python pick a number and dont tell me about it 
secret_number = random.randint(1, 10)
#input the number you want 
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("You guessed it right!")
else:
    print("The correct number was", secret_number)