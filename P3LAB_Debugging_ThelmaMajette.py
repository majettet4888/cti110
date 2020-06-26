# Correcting a partial program with bugs
# CTI - 110
# P3LAB - Debugging
# Thelma Majette
# 25 Jun 20
#

# Input test score
score = float(input( 'Enter your test score: ' " " ))

# Identify the grade with the score
A_score = 90 - 100
B_score = 80 - 89.9
C_score = 70 - 79.9 
D_score = 65 - 69.9 
F_score = 64 

# Display the Grade
if score >= 90:
              print ( 'Your grade is A.' )
elif float(score >= 80 and float(score <= 89.9)):
              print ( 'Your grade is B.' )
elif float(score >= 70 and float(score <= 79.9)):
              print ( 'Your grade is C.' )
elif float(score >= 65 and float(score <= 69.9)):
              print ( 'Your grade is D.' )
else: 
              print ('Your grade is F.' )
              
              

