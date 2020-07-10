# Random number guessing game.
# 10 July 20
# CTI-110 P5HW1 - Random Number
# Thelma Majette

import random

randomNumber = random.randint (1,100)

# main function
def main():

      # Create a variable to control the loop.
      keep_going = 'y'
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
            
                    
             
main ()                                                         
