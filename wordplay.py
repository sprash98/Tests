



def count_words() :
    f = open('C:\\Temp\\words.txt')


    words = {}
    for line in f:
        for word in line.split():
            print("Word is %s" %(word))
            if word not in words.keys() :
                words[word] = 1

    print("Total number of unique words in file is %d" %(len(words.keys())))

def rep(s,char,newchar,count,n) :

    index = s.find(char)
    if index < 0:
        if count == 0:
            print("Character %c not found in string %s" %(char,s))
        return s

    count += 1
    if count == int(n):
        s= s.replace(char,newchar,1)
        return s
    else:
        s = s[:index+1]+rep(s[index+1:],char,newchar,count,n)

    return s


init = 1
count = 0
st = raw_input("Enter a string\n")
char = raw_input("Enter character to be replaced\n")
newchar = raw_input("Enter replacement character\n")
occurrences = raw_input("Enter occurrence of character to be replaced\n")
st = rep(st,char,newchar,count,occurrences)
print("Replaced string is %s"%(st))




