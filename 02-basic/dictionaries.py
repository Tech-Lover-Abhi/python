chai_types = {"Masala":"Spicy", "Ginger":"Zesty", "Green":"MIld"}

# CHECK VALUE
# print(chai_types["Masala"])

# CHECK VALUE
# print(chai_types.get("Ginger")) # Zesty # get mathod

# CHANGE VALUE
chai_types["Green"] = "Fresh" # Change the value 
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# ADD
chai_types["Earl Grey"] = "Citrus" # ADD key value
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# POP
chai_types.pop("Ginger") # Remove item 
print(chai_types)  # {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# pop
chai_types.popitem() # Remove last item 
print(chai_types) # {'Masala': 'Spicy', 'Green': 'Fresh'}

# DELET
del chai_types["Green"] # Delet item
print(chai_types) # {'Masala': 'Spicy'}

# COPY
# chai_types_copy = chai_types.copy() # copy AS it is an another memory location
# print(chai_types_copy)

tea_shop = {
    "Chai": {"Masala":"Spicy", "Ginger":"Zesty"},
    "Tea": {"Green":"Mild", "Black":"Strong"}
}
print(tea_shop)
print(tea_shop["Chai"]) # {"Masala":"Spicy", "Ginger":"Zesty"}
print(tea_shop["Tea"]) # {"Green":"Mild", "Black":"Strong"}
print(tea_shop["Chai"]["Ginger"]) # Zesty

# Found squired
squired_num = {x:x**2 for x in range(6)}
print(squired_num) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# clear squired
squired_num.clear()
print(squired_num) # {}

# Create dictinary for morje ( key, value )
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value) # {'Masala':'Delicious', 'Ginger':'Delicious', 'Lemon':'Delicious'}
print(new_dict)

# for chai in chai_types: # print key
    # print(chai)


# for chai1 in chai_types: # print key and value
    # print(chai1, chai_types[chai1])


# for key, values in chai_types.items(): # That also be print key and values
    # print(key, values)


# for chai2 in chai_types: # print value
    # print(chai_types[chai2])


# IF ELSE condition
# if "Masala" in chai_types: # if else condition
    # print("I LOVE MASALA CHAI")
# else:
    # print("NOT FOUND")


# IF ELSE condition
# AB = 20 # if else condition 
# if (AB >= 18):
    # print("I AM ADULT")
# else:
    # print("I AM NOT ADOLT")







