
input_str = "Abhijit"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break

    # if input_str.count(char) >= 2:
        # print("Repeted char is: ", char)