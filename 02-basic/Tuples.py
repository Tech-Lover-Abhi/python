
# you can do all the task which you do in list

tea_types = ("Black", "Green", "Oolong")
print(tea_types[0]) # Black
print(tea_types[-1]) # Oolong
print(tea_types[1:]) # ('green', 'Oolong')
# tea_types[0] = "Lemon" # Error
# print(tea_types) # Error ( because this is immutable )

print(len(tea_types)) # 3

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types # morje all tuples
print(all_tea) # ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')


# count duplecat value ( double item )
more_chai = ("Herbal", "Earl Grey", "Herbal") # Herbal is 2 time enter
print(more_chai.count("Herbal")) # 2

# un rap tuples
(black, green, oolong) = tea_types
print(black) # Black
print(green) # Green
print(oolong) # Oolong

# Type
print(type(tea_types))  # <class 'tuple'>


# Nasted Tuaples
("", (1, 2, 3), "")

