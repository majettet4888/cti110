# Outcome of mixing two primary colors
# CTI-110
# P3HW1 - Color Mixer
# Thelma Majette
# 24 Jun 20
#


# Input primary color 1
primaryColor1 = input( "Enter primary color 1: " )

# Input primary color2
primaryColor2= input( "Enter primary color 2: " )

# Color mixture
purple = primaryColor1 + primaryColor2 
orange =  primaryColor1 + primaryColor2 
green = primaryColor1 + primaryColor2 

# Determine the outcome of mixing two colors
if primaryColor1 == "red"  and  primaryColor2 == "blue" or primaryColor1 =="blue"  and  primaryColor2 == "red":
              print ('Purple')
elif primaryColor1 == "red"  and  primaryColor2 == "yellow" or primaryColor1 == "yellow"  and  primaryColor2 == "red":
              print ('Orange')
elif primaryColor1 == "blue"  and  primaryColor2 == "yellow" or primaryColor1 == "yellow" and primaryColor2 == "blue":
              print ('Green')
else: print ('Error: secondary color doesn\'t match')

