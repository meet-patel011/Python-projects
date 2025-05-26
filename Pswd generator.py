import random
import string

pswd_len = 12
charValues = string.punctuation + string.ascii_letters + string.digits

Password = ""
for i in range (pswd_len):
    Password += random.choice(charValues)

print("Your password is:", Password)    