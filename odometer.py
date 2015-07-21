


def pali_check(n) :

    if len(n) <= 1:
        return 1

    if n[0] == n[-1] :
        return pali_check(n[1:-1])
    else :
        return 0



def odometer () :

    for i in range(100000,999999) :
        #if pali_check(str(i)[1:-1]) :
        if pali_check(str(i)[-4:]) and pali_check(str(i+1)[-5:]) and pali_check(str(i+2)[1:-1]) and pali_check(str(i+3)) :
            print ("The number we seek is %d!" %(i))


    return 1



odometer()


