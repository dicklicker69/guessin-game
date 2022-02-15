import random #imports random number

MIN_NUMBER = 1    #Minimum number
MAX_NUMBER = 20   #Maximum number

random_number = int(random.randint(MIN_NUMBER, MAX_NUMBER)) 
#Makes random number a value

print(random_number) # Prints random number for error checking will not be in final ver

while True: 

    user_answer = int(input('guess a number bettween {} and {}  : '.format(MIN_NUMBER, MAX_NUMBER)))
  #gives user answer a value and asks main question

    if(user_answer == random_number): 
        print('you have guessed the number !!!!')
        break
      #Ends game if user answer is correct
    
    elif(user_answer > random_number): 
       print('that number is too big')
  #Gives user another chance at answering and also tells them the number is to big
  
    elif(user_answer < random_number): 
        print('that number is too small')
  #Gives user another chance at answering and also tells them the number is to small

    
  
      






