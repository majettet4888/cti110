# Converts kilometers to miles.
# 7 July 20
# CTI-110 P5T1_KilometerConverter
# Thelma Majette

# Convert kilometers to miles
CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.
def main () :
              # Get the distance in kilometers.
              kilometers = float(input (' Enter a distance in kilometers: ' ))

              # Display the distance converte to miles.
              show_miles (kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.

def show_miles (km):
              # Calculate miles.
              miles =  km * CONVERSION_FACTOR

              # Display the miles.
              print (km, ' kilometers equals ',  miles, ' miles. ')

# Call the main function.
main ()


