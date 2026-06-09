import random
import string

length = int(input("Enter required length of the password: "))

characters = string.ascii_letters + string.punctuation + string.digits

password = ""
for i in range(length):
    password += random.choice(characters)
print("Generated password: ", password)
