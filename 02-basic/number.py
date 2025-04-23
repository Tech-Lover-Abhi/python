x = 2
y = 3
z = 4
print(x + y) # 5
print((x + y) * z) # 20
print(x, y, z) # 2, 3, 4 
print(x + 1, y * 2) # 3, 6
print(y % 2) # remandor 1
print(z ** 2) # power 16
print(40 + 2.23) # 42.23 # dont do that because always remamber both the data type want most be same data type
print(int(2.23)) # 2 # It convert float number to int number
print(float(40)) # 40.0 # It convert to int number to float number
print('Abhijit' + ' Nayak') # Abhijit Nayak # this is a operator over loading ( It is concatenate the 2 strings) and it is check the data type
## repr('Abhi')
## str('abhi')
print(x < y < z) # true ( x < y and y < z) if both argument are true then ansure is true
print(1 == 2 < 3) # false ( 1 == 2 and 2 < 3) if one argument is false then ansure false

import math
print(math.floor(3.5)) # 3 # the floor() mathod alwaya gives the ground value
print(math.floor(-3.5)) # -4
# print(math.trunc(2.8)) # dout

import random
print(math.floor((random.random() * 10 + 1))) # 4, 5, 7 ,8 ( generate random number in one degits )
print(random.randint(1, 10)) # 5, 6, 8 ( that also genorate the random number up to 1, 10 ) 

l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1)) # it is randomly choice any string in this l1 list
print(random.shuffle(l1)) # ['lemon', 'masala', 'ginger', 'mint'], ['ginger', 'lemon', 'masala', 'mint'] it is continuasly mix the li like tass patta
print(l1) # call li



print(0.1 + 0.1 + 0.1) # 0.30000000000000000  (like that)
print(0.1 + 0.1 + 0.1 - 0.3) # 5.551115123125783e-17  ( un accepted ansure [ wrong ansure ] )

from decimal import Decimal # This is the write way to calculate the floot number

print( Decimal('0.1') + Decimal('0.1') + Decimal('0.1') ) # 0.3 
print( Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # 0.0 



###################################### SET ##################################

setone = {1, 2, 3, 4}
print(setone & {1, 3})  # {1, 3} intersaction [ comon lator]
print(setone | {1, 2}) # {1, 2, 3, 4} union
print(setone - {1, 2, 3, 4}) # set() [ delet ]


