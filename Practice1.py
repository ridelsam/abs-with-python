import random

print('Enter your name')
Player1 = str(input())

MaxGuess=6
count=0

print('Yo ' + str(Player1) + '! I have an integer between 1 and 20.\nYou only have ' + str(MaxGuess) + ' guesses')


num=random.randint(1,20)



while count<MaxGuess:
    
    userInput=input()
    
    try:
        if int(userInput)<num:
            print('Guess is too low')
        elif int(userInput)>num:
            print('Guess is too high')
        elif int(userInput)==num:
            print('Noiiceee')
            break
        
        count=count+1
        GuessLeft=MaxGuess-count
        if count == MaxGuess:
            print('Game Over foo')
            print('Answer was ' + str(num))
            break
        else:
            print('You have ' + str(GuessLeft) + ' guess(es) left. Try Again')
            
    except ValueError:
        print('Must be an integer')
        continue

        
print('end')



