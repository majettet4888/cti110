# Displaying a stair step pattern using nested loop
# 2 July 20
# CTI-110 P3HW3 - Nested Loops
# Thelma Majette

# Number of rows
num_steps = 6

# Use the outer loop for the number of rows
for r in range (num_steps):
              
              # print the first " # " in each row
              print (' # ', end=' ')

              # Use the inner loop to print spaces
              for c in range (r):
                            if (c!=r):
                                          print (' ', end=' ' )
                                          
              # Print the last " # " in each row
              print (' # ')

              

