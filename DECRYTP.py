# Christian Dating | BSCPE 1-5

import pyfiglet

input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" *80)

#Intro
greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "bubble"))

print("\033[90m=" *80)







# Problem 2 - Decryption
input_str = input("\033[94mPlease enter a string to decrypt: ")
output_str = ""

for i in range(len(input_str)):
    if input_str[i] == "*":
        output_str += "a"
    elif input_str[i] == "&":
        output_str += "e"
    elif input_str[i] == "#":
        output_str += "i"
    elif input_str[i] == "+":
        output_str += "o"
    elif input_str[i] == "!":
        output_str += "u"
    else :
        output_str += input_str[i]
    
print("\n\033[98mYour string: ", input_str)
print("\n\033[98mThe Plain Text: ", output_str)

print("\033[90m=" *80)

# Outro
greet1 = "THANK YOU!"
print("\033[92m" + pyfiglet.figlet_format(greet1, font = "bubble"))

print("\033[90m=" *80)