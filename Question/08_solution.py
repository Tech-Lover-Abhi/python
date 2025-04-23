Enter_password = "Abhijit nayak"
password_length = len(Enter_password)

if ( password_length <= 6 ):
    password = "Weak"
elif ( password_length <= 10 ):
    password = "Medium"
elif ( password_length > 10 ):
    password = "Strong"

print("Your password strength is", password)