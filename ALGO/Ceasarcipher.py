import string

def cipher(a_string, key):
    upperCase = string.ascii_uppercase  #'abcdefghijklmnopqrstuvwxyz'
    lowerCase = string.ascii_lowercase  #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encrypt = ''

    for i in a_string:
        if i in upperCase:
            new = (upperCase.index(i) + key) % 26  
            encrypt +=upperCase[new]

        elif i in lowerCase:
            new = (lowerCase.index(i) + key) % 26 # mod is 6 
            encrypt +=lowerCase[new]
        else:
            encrpt+= i

    return encrypt


a_string = "abcdefg"
key = 3
decipher = cipher(a_string, key)
print(decipher)

