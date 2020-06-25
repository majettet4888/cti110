# Basic math calculator asking user to display a choice from the menu
# 24 June 2020
# CTI-110 P3HW2 - Basic Math Calculator
# Thelma Majette
#

# Create menu
print ( "-------- Menu -------" )
print ( "1) Add Numbers" )
print ( "2) Multiply Numbers" )
print ( "3) Subtract Numbers" )
print ( "4) Exit" )
print ( "------------------------" )

       
# Get the first number to calculate
first_number = int(input ( 'Enter the first number: '  " ")) 

# Get the second number to calculate
second_number = int(input ( 'Enter the second number: ' " " ))

# Enter a number from the menu choice
menuChoice = input( 'Enter menu choice: ' " " ) 

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
else: print ( 'Error: Incorrect choice was entered' )

