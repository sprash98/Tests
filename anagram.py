


def anagram_check(w1,w2) :

    l1= list(w1)
    l2= list(w2)

    count1 = {}
    count2 = {}

    for c in l1:
        if c in count1 :
            count1[c] +=1
        else:
            count1[c] = 1

    for c in l2:
        if c in count2:
            count2[c] +=1
        else:
            count2[c] = 1

    for i in count1 :
        if i not in count2:
            print("Letter %c not in '%s'" %(i,w2))
            return 0

        if count1[i] != count2[i] :
            print("Count mismatch for character %c. Found %d in %s and %d in %s" %(i,count1[i],w1,count2[i],w2))
            return 0

        count2.pop(i)

    if len(count2) :
        print("The following characters are not in string %s: %s" %(w1,",".join(str(i) for i in count2)))
        return 0

    return 1


def anagram_count() :

    f = open("C:\\Temp\\words.txt",mode='r')

    anagrams = {}

    for word in f :
        chars = tuple(word)

        ana_list = []




def meta_check(w1,w2) :

    if not anagram_check(w1,w2) :
        print("The words '%s' and '%s' are not a metathesis pair as they are not anagrams"%(w1,w2))
        return 0

    diff= 0

    for k,j in zip(w1,w2) :
        if k !=j :
            diff+= 1

    if diff !=2:
        print("Words '%s' and '%s' are not a metathesis pair as they have %d letters swapped" %(w1,w2,diff))
        return 0

    print("Words '%s' and '%s' are a metathesis pair" %(w1,w2))
    return 1


words = raw_input("Enter the words to be checked, separated by a comma: ")
(w1,w2) = words.split(',')
if not anagram_check(w1,w2) :
    print("The words %s and %s are not anagrams" %(w1,w2))
else:
    print("The words %s and %s are anagrams" %(w1,w2))

meta_check(w1,w2)



