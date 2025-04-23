
Distance = 44

if ( Distance <= 3 ):
    travel = "Wallk"
elif ( Distance <= 15 ):
    travel = "Bike"
elif ( Distance > 15):
    travel = "Car"

print("AI recommends you the transport of:", travel)

