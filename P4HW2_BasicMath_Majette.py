# Basic math calculator asking user input from the menu
# CTI-110
# P4HW2 - BasicMath 
# Thelma Majette
# 2 July 2020

def main ():
              keep_going = 'y'
              while keep_going == 'y':
                            
                            # Print menu
                            print ( '\nMenu' )
                            print ( '  1.  Add Numbers' )
                            print ( '  2.  Multiply Numbers' )
                            print ( '  3.  Subtract Numbers' )
                            print ( '  4.  Exit' )
                            print ()

                            # Get the first number to calculate
                            first_number = int(input ( 'Enter the first number: '  " "))

                            # Get the second number to calculate
                            second_number = int(input ( 'Enter the second number: ' " " ))

                            # Enter a number from the menu choice
                            menuChoice = input( 'Enter menu choice: ' " " )
                            print ()

                            # Calculate the sum of both numbers
                            sum = first_number + second_number

                            # Calculate by multiplying both numbers
                            multiply = first_number * second_number

                            # Calculate by multiplying both numbers
                            subtract = first_number - second_number

                            # Display results from the menu choice
                            if menuChoice == "1":
                                          print ( 'Menu choice 1 is:', format(sum, ',.2f'), sep=' ')

                            elif menuChoice == "2":
                                          print ( 'Menu choice 2 is:', format(multiply, ',.2f'), sep=' ')

                            elif menuChoice == "3":
                                          print ( 'Menu choice 3 is:', format(subtract, ',.2f'), sep=' ')

                            elif menuChoice == "4":
                                            print ('Menu choice 4: Exit program')
                                            keep_going = 'n'

                            else:
                                          print ( 'Incorrect choice was entered. Please choose from the menu.' )
                                          input( 'Press any key to continue.' )

main ()


