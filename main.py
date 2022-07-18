import random
import string

length = int(input('Enter the length of your password: '))
name_of_website = input('Enter the name of the website/app: ')
filename = input('Enter the name of the file in which you want the password to be saved: ')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

everything = upper + lower + num + symbols

temp = random.sample(everything,length)

password = "".join(temp)

print("Your generated password for " + name_of_website + " is " + password + " and is now stored in the file which was entered by you")
with open(filename, 'w') as file:
    file.write("Your generated password for " + name_of_website + " is " + password)


