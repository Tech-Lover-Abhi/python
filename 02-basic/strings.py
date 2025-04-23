chai = "Masala Chai"
first_char = chai[0]
# print(first_char)
slice_chai = chai[0:6]
# print(slice_chai)

num_list = "0123456789"
# print(num_list[:]) # 0123456789
# print(num_list[3:]) # 3456789
# print(num_list[:3]) # 012
# print(num_list[3:3]) # empty
# print(num_list[3:6]) # 345
# print(num_list[0:7:2]) # 0246 [ ( 2 ) jump 2 number]

# print(chai.lower()) # masala chai
# print(chai.upper()) # MASALA CHAI
# print(len(chai)) # 11 # length of the string
# print(chai.find("Chai")) # 7 # [ which position the chai is avaliable ]


name = '    Abhijit     '
# print(name.strip()) # cut the spaces
# print(name) # not cut the spaces

# print(chai.replace("Masala", "Ginger")) # Ginger Chai [ replace the Masala name to Ginger]
# print(chai.removeprefix("Masala")) # remove the Masala name


tea = "Lemon, Ginger, Masala, Mint"
# print(tea.split(", ")) # ['Lemon', 'Ginger', 'Masala', 'Mint'] change the format


chai_count = "Lemon Chai Chai Chai Chai Chai Chai Chai"
# print(chai_count.count("Chai")) # 7 # count the Chai repetation number



chai_type = "Masala"
quentity = 2
order = "I ordered {} cups of {} chai" # {} - place holder
# print(order.format(quentity, chai_type)) # I ordered 2 cups of Masala chai [ it is put ta value in place holder ]

chai_variety = ["Lemon", "Masala", "Ginger"] # list of chai variety
# which type of data you want just put on the ( "" ) under the doble Cotation
# print("".join(chai_variety)) # LemonMasalaGinger [ joint all the list item ]
# print(" ".join(chai_variety)) # Lemon Masala Ginger [ joint all the list item with space ]
# print("-".join(chai_variety)) # Lemon-Masala-Ginger [ joint all the list item with ( - ) ] 
# print(", ".join(chai_variety)) # Lemon, Masala, Ginger [ joint all the list item with ( ,  ) ] 

tips = "He said, \"Masala chai is awesome\" " #  It isa write process to wright this [ path process ]
print(tips) # He said, "Masala chai is asesome"

chai1 = "Masala\nChai"
print(chai1) # Masala ( down line ) Chai
chai2 = r"Masala\nChai" # (r) for row string
print(chai2) # Masala\nChai [ as it is ]

url = r"c:\user\pwd" # (r) right way [ with row string ]
print(url) # c:\user\pwd

# url1 = "c:\user\pwd" # without r create problem
# print(url1) # In this process tha error will be ocered

url2 = "c:\\user\\pwd" # without (r) solution
print(url2)


# Asking question
chai3 = "Abhijit Nayak"
print("Abhijit" in chai3) # True
print("Abhijitt" in chai3) # False



