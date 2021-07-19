"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import random
import string
ptype=input('Enter type of password : ')

weakpswd=['ab78','hg3hG','fhfj21']
if ptype=='weak':
    print(random.choice(weakpswd))


else:
    nums='123456789'
    low='abcdefghijklmnopqrstuvwxyz'
    up=low.upper()
    chars='@_$#~&^'
    size=8 
    pswd=nums+low+up+chars
    password="".join(random.sample(pswd,size))
    print(password)
    


