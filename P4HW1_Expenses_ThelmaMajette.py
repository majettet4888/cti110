# Calculate  accumulated expenses.
# CTI-110
# P4HW1- Expenses
# Thelma Majette
# 2 July 20


# initialize an accumulate variable
total_expense = 0
user_expense = 0
num_expense = 0

# total_expense -= user_expense
# num_expense += user_expense

# Prompt user to enter starting amount to be withdrawn.
start_amount = int(input( 'Enter starting amount in account : '))
print (" ")

# Create a variable to control the loop
keep_going = 'y'
while keep_going == 'y':

    # Prompt user to enter expense
    user_expense = int(input( 'Enter expense: '))
    #total expenses and iterations of loop
    total_expense += user_expense
    num_expense += 1

    # See if user wants to enter another expense
    # assiggn y/n to keep_going
    keep_going = input ('Do you want to enter another expense? Enter y/n ' )
    print ()

# if keep_going!= ' Y':
# got final account amount and then displayed everything
finalAccountAmt = start_amount - total_expense
print ('Amount in account before expense subtraction $', format (start_amount, ',.2f' ))
print ('Number expenses entered:', num_expense)
print ()
print ('Amount in account After expenses subtracted is $',  format (finalAccountAmt, ',.2f'))







									  






	   





			   



