

import string
import os

table = dict()
print(os.path)
def count(f) :

    global table
    for char in string.ascii_uppercase :
        table[ord(char)] = char.lower()


    for key in table:
        print("Key is %s, and value is %s" %(key,table[key]))


    punc = string.punctuation

    'ABC'.translate(table)
    words = []
    for l in f:
        for mark in punc :
            l = l.replace(mark,' ')

        line_words = l.split()

        for word in line_words:
            words.append(word.translate(table))



    return words


def print_words(words):

    i = 1
    for word in words :
        print("Word %d is %s" %(i,word))
        i+= 1

    return 1


f = open("C:\\Temp\\lines.txt")
words =count(f)
print_words(words)



