
order_size = "medium"
extra_shot = True

if extra_shot:
    coffee = order_size + "coffee with extra shot"
else:
    coffee = order_size + "coffee"

print("Order: ", coffee)