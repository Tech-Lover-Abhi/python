
# Fruit = "Banana"
Banana = "Brown"

# color = "Green", "Yellow", "Brown"

if ( Banana == "Green"):
    fruit = "Unripe"
elif ( Banana == "Yellow"):
    fruit = "Ripe"
elif ( Banana == "Brown"):
    fruit = "Overripe"
else:
    fruit = "Not usabled"

print("Banana is", fruit)

# Another one

fruit = "Banana"

color = "Brown"

if ( fruit == "Banana"):
    if ( color == "Green"):
        print("Unripe")
    elif ( color == "Yellow"):
        print("Ripe")
    elif ( color == "Brown"):
        print("Overripe")
else:
    print("This frout details is not avaliable")