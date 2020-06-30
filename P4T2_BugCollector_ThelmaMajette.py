# Find out how many bugs were collected for five days.
# 30 June 20
# CTI-110 P4T2 - Bug Collector
# Thelma Majette
#

# Initialize an accumulator variable.
total = 0

# Get the bugs collected for each day.
for day in range (1, 6):
              
              # Prompt the user.
              print ( 'Enter the bugs collected on day', day)

              # Input number of bugs.
              bugs = int (input () )

              # Add bugs to total.
              total += bugs



# Display the total bugs.
print ( 'You collected a total of' , total, ' bugs. ' )

