import random

MIN_NUMBER = 1
MAX_NUMBER = 20 

random_number = int(random.randint(MIN_NUMBER, MAX_NUMBER))

print(random_number)

while True: 

    user_answer = int(input('guess a number bettween {} and {}  : '.format(MIN_NUMBER, MAX_NUMBER)))

    if(user_answer == random_number): 
        print('you have guessed the number !!!!')
        break
    
    elif(user_answer > random_number): 
        print('that number is too big')

    elif(user_answer < random_number): 
        print('that number is too small')