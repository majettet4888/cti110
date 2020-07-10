# Part 2:  Menu driven random number guessing game.
# 10 July 20
# CTI-110 P5HW1 - Random Number
# Thelma Majette

import random

# Displays the menu function
def display_menu ():
          print ('\nMenu')
          print ('----------------')
          print ('1.  Play Game')
          print ('2.  Exit')

# The main function
def main ():
    continuePlay = 'y'
    while continuePlay == 'y':
    
        # Display menu
        display_menu ()

        # Get the user's choice.
        choice = input('\nSelect from menu: ')

        # Create a variable to control the loop.
        if choice == '1':
            gamePlay()
        elif choice == '2':
            continuePlay = 'n'
        else:
            print('Error, please select a choice')
        
def gamePlay ():
    
      # Create a variable to control the loop.
      keep_going = 'y'
      randomNumber = random.randint (1,100)

      # Continue the loop.
      while keep_going == 'y':

            # Ask user for a number ()
            guess = int(input('\nGuess a number between 1 and 100: '))

            # Perform the selected action.
            if guess > randomNumber:
                print ('\nToo high, try again.' )
            elif guess < randomNumber:
                print ('\nToo low, try again' )
            else:
                print ('\nCongratulations, you guessed the correct number!')
                keep_going ='n'
            


# Call the main function.
main ()



              
 

              
              














