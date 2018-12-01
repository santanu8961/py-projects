# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random 
vowels = 'aeiou'
consonents = 'bcdfghjklmnpqrstvwxyz'
letter1 = input('Enter "c" for consonats & "v" for  vowels : ')
letter2 = input('Enter "c" for consonats & "v" for  vowels : ')
letter3 = input('Enter "c" for consonats & "v" for  vowels : ')
letter4 = input('Enter "c" for consonats & "v" for  vowels : ')
letter5 = input('Enter "c" for consonats & "v" for  vowels : ')
def generator(letter):
    if letter == 'v' :
        l = random.choice(vowels)
    elif letter == 'c' :
        l =  random.choice(consonents) 
    else : l = letter
    return(l)
    
print('Here are 20 baby name suggesions for u : ')    
    
for babyname  in range(10):
    name = generator(letter1) + generator(letter2) + generator(letter3) + generator(letter4) + generator(letter5)

    print(name)

        
        

    
#print(generator())
    



    
    
