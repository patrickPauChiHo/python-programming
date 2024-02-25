import random   
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print_message = input("Enter the message: ")
encrypted_message = ""

for char in print_message:
    index = chars.index(char)
    encrypted_message += key[index]
    
print(encrypted_message)

# print(chars)
 #print(key)