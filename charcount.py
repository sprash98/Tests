

from sys import *




def counter(str,char,init=0,index=0,count=0) :

    if str != '' :
        if str.find(char) >=0 :
            count +=1
            if str.index(char) ==0:
                index += 1
            #elif str.index(char) >0 and init:
                #index += str.index(char)
                #init = 1
            else:
                index += str.index(char) + 1

            print("Occurrence %d of character '%c' in string is %d" %(count,char,index))
            str=str[str.index(char)+1:]
            return counter(str,char,init,index,count)
        else :
            if not count:
                print("Char '%c' not found in string %s" %(char,str))

        return 1


counter('seasons','s')



