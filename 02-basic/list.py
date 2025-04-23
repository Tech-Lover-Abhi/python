tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[2])
tea_varities[3] = "Herbal" # replace process
print(tea_varities[3])
print(tea_varities)  # ["Black", "Green", "Oolong", "Herbal"]

print(tea_varities[1:2]) # ['Green']
# tea_varities[1:2] = "Lemon" # string format data
# print(tea_varities) # ['Black', 'L', 'e', 'm', 'o', 'n', 'oolong', 'White']


tea_varities[1:2] = ["Lemon"] # Array format
print(tea_varities) # ['Black', 'Lemon', 'Oolong', 'White']

# REPLACE
tea_varities[1:3] = ["Green", "Masala"] # Replace 2 item at a time
print(tea_varities) # ['Black', 'Green', 'Masala', 'White']

# INSURT
tea_varities[1:1] = ["Abhi", "Abhijit"] # Insurt/ Add 2 item [ indx no 1 ]
print(tea_varities) # ['Black', 'Abhi', 'Abhijit', 'Green', 'Masala', 'White']

# DELEET
# tea_varities[1:3] = [] # Empty Array # Insert [] in this 2 item [ delet format ]
# print(tea_varities) # ['Black', 'Green', 'Masala', 'White']

# APPEND
tea_varities.append("Masala") # Add in last item [ Masala ]
print(tea_varities) # ['Black', 'Green', 'Oolong', 'White', 'Masala']

# POP
tea_varities.pop() # Remove last item [ Masala ]
print(tea_varities) # ['Black', 'Green', 'Oolong', 'White']

# Remove
tea_varities.remove("Green") # Remove any item you want
print(tea_varities) # ['Black', 'Oolong', 'White']

# ADD
tea_varities.insert(1, "Green") # Add item which index you want and what item
print(tea_varities) # ['Black', 'Green', 'Oolong', 'White']

# COPY
# If you try to change somthing in your copy list, the original list not be affected
tea_varities_copy = tea_varities.copy() # output is same but memory location is differente 
print(tea_varities_copy) # ['Black', 'Green', 'Oolong', 'White']


# if "Masala" in tea_varities: # check condition 
    # print("I have Masala Tea") # I have Masala Tea


Squared_num = [x**2 for x in range(10)]
print(Squared_num) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Squared_num1 = [y**3 for y in range(10)]
print(Squared_num1) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]




