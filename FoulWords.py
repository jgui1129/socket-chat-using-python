'''
Created on May 12, 2017

@author: Administrator
'''
from random import randint

def filter(words):
    x = words.split()
    temp = ""
    for a in range(len(x)):
        temp += converFoulWords(x[a]) + " "

    return temp

def converFoulWords(x):
    list = ["abnoy","tanga"]
    specialChar = ["*","@","#","!","~","^","%","*","!","&","*","@","#","$","#","<",">","?","+","!"]
    
    word = ""
    filteredWords = ""
    if x.lower() in list:
        for a in list:
            if a == x.lower():
                count = len(x)
                for b in range(count):
                    pos = (randint(0,18))
                    word+=specialChar[pos]
        filteredWords +=  x[0] + word
    else:
        filteredWords += x.lower()
    
    return filteredWords

