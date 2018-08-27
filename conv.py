
low = {'11': 'eleven', '10': 'ten', '13': 'thirteen', '12': 'twelve', '15': 'fifteen', '14': 'fourteen', '17': 'seventeen', \
        '16': 'sixteen', '19': 'nineteen', '18': 'eighteen', '1': 'one', '0': 'zero', '3': 'three', '2': 'two', '5': 'five', '4': 'four', \
         '7': 'seven', '6': 'six', '9': 'nine', '8': 'eight'}

ties = {'3': 'thirty', '2': 'twenty', '5': 'fifty', '4': 'forty', '7': 'seventy', '6': 'sixty', '9': 'ninety', '8': 'eighty'}

def conv(num,trans=str()):
    if int(num) < 20 :
        if trans and num!= '0':
            trans += low[num]
            return trans
        elif not trans:
            return low[num]
    else :
        if ((int(num)/(10**6) < 10**6) and (int(num)/(10**6) >= 1))   :
            high_pos = int(num)/(10**6)
            trans += conv(str(high_pos),trans)+' million '
            trans +=conv(str(int(num)%(10**6)),trans)
        elif (((int(num)/(10**6)) < 1) and (int(num)/1000) >= 1) :
            high_pos = int(num)/1000
            trans += conv(str(high_pos),trans)+' thousand '
            trans +=conv(str(int(num)%1000),trans)
        elif ((int(num)/1000) < 1) and (int(num)/100 >=1) :
            high_pos = int(num)/100
            trans += conv(str(high_pos),trans)+' hundred '
            trans +=conv(str(int(num)%100),trans)
        elif (int(num)/100) < 1:
            high_pos = int(num)/10
            if trans :
                trans += 'and '
            trans += ties[str(high_pos)]+conv(str(int(num)%10),trans)
            
        return trans

print(conv('45000'))
