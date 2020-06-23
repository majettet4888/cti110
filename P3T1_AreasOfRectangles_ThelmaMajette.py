# Determine which rectangle has the greater area
# 23 June 20
# CTI-120 P3T1 - Areas of Rectangles
# Thelma Majette


# Input the length and width of rectangle 1.
lengtha = int(input("Enter the length of rectangle a: "))
widtha = int(input("Enter the width of rectangle a: "))

# Input the length and width of rectangle 2.
lengthb = int(input("Enter the length of rectangle b: "))
widthb = int(input("Enter the width of rectangle b: "))

# Calculate the area of rectangle 1.
area1 = lengtha * widtha

# Calculate the area of rectangle 2.
area2 = lengthb * widthb

# Determine which has the greater area.
if area1 > area2:
              print ("Rectangle a has the greater area.")
elif area2 > area1:
              print ("Rectangle b has the greater area.")
else:
              print ("Both have the same area.")

                         


