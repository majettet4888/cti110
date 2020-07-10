# Adding random numbers 
# 10 July 20
# CTI-110 P5HW2 - Math Quiz
# Thelma Majette

import random

def main ():

    randomNumber1 = random.randint (1, 250)
    randomNumber2 = random.randint (1, 250)

    # Ask user to input the sum of two random numbers.
    userAnswer = int(input( 'What is '  +   str(randomNumber1)  +   " + "   + str(randomNumber2)  + ' ? :  '))

    # Calculate the random numbers.
    add = randomNumber1 + randomNumber2

    # Perform the selected action.
    if userAnswer == add:
        print('Congratulations!')
    else:
        print('Incorrect answer. The correct answer is: ', add)




main ()

    
