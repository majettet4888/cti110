# Menu driven adding and subtracting random numbers (Part 2)
# 10 July 20
# CTI-110 P5HW2 - Math Quiz
# Thelma Majette

import random

# Display the menu function.
def display_menu ():
    print ('\nMenu')
    print ('----------------')
    print ('1.  Add Random Numbers')
    print ('2.  Subtract Random Numbers')
    print ('3.  Exit')
    print ()
    
# Display the main function.
def main ():
    continuePlay = 'y'
    while continuePlay == 'y':
        
        # Display menu
        display_menu ()

        # Get the user's choice.
        choice = input('\nSelect from menu:  ')

        # Creat a variable to control the loop.
        if choice == '1':
            add ()
        elif choice == '2':
            subtract ()
        elif choice == '3':
            continuePlay = 'n'
        else:
            print('Error, please select a choice')

def add ():
    randomNumber1 = random.randint (1,250)
    randomNumber2 = random.randint (1,250)

    # Calculate answer.
    add = randomNumber1 + randomNumber2
    
    # Ask user to input the sum of two random numbers.
    userAnswer = int(input( 'What is '  +   str(randomNumber1)  +   " + "   + str(randomNumber2)  + ' ? :  '))

    # Perform selected action.
    if userAnswer == add:
        print('Congratulations!')
    else:
        print('\nIncorrect answer. The correct answer is: ', add)
        
def subtract ():
    randomNumber1 = random.randint (1,250)
    randomNumber2 = random.randint (1,250)

    # Calculate the answer.
    subtract = randomNumber1 - randomNumber2
    
    # Ask user to input the difference of two random numbers.
    userAnswer = int(input( 'What is '  +   str(randomNumber1)  +   " - "   + str(randomNumber2)  + ' ? :  '))

    # Perform selected action.
    if userAnswer == subtract:
        print('Congratulations!')
    else:
        print ('\nIncorrect answer. The correct answer is: ', subtract) 
    

# Call the main function.
main ()
