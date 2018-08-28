
# Function to convert a given number specified as an integer string, to it's worded 
# equivalent. That is, when the user feeds the function a number such as '234', 
# the function returns 'two hundred thirty four'

from collections import OrderedDict
from pip._vendor.distlib.compat import raw_input

#Dictionary containing the mappings upto the first nineteen numbers
low = {'11': 'eleven', '10': 'ten', '13': 'thirteen', '12': 'twelve', '15': 'fifteen', '14': 'fourteen', '17': 'seventeen', \
        '16': 'sixteen', '19': 'nineteen', '18': 'eighteen', '1': 'one', '0': 'zero', \
         '3': 'three', '2': 'two', '5': 'five', '4': 'four', '7': 'seven', '6': 'six', '9': 'nine', '8': 'eight'}

# Dictionary defining the numbers beginning with 'ty', ala twenty 
ties = {'3': 'thirty ', '2': 'twenty ', '5': 'fifty ', '4': 'forty ', '7': 'seventy ', '6': 'sixty ', '9': 'ninety ', '8': 'eighty '}

# List describing the 'places' or positions of numbers in numeric format
num_units = [10**9,10**6,1000,100]

# List describing the positions in alphabetic format
alpha_units = ['billion','million','thousand','hundred']

# Ordered dictionary containing the mapping of numeric positions to 
# the alphabetic counterparts               
units = OrderedDict([i,j] for i,j in zip(num_units,alpha_units))

def conv(num,trans=str()):
    
    # For numbers less than twenty, return it's string equivalent
    if int(num) < 20 :
        if trans:
            if num != '0':
                return low[num]
            else :
                return ''
        

        return low[num]
    else :
        # For numbers greater than 20, figure out the positions of the digits
        ukeys = list(units.keys())
        
        while (int(num) !=0):
            
            # Determine the position of the digits by dividing the number
            # successively by 10 raised to the power of the position, 
            # starting from the billionth position
            
            for k in range(0,len(ukeys)-1) :
                if ((int(num)//ukeys[k] < 1) and (int(num)//ukeys[k+1] >= 1))   :
                    high_pos = int(num)//ukeys[k+1]
                    trans += conv(str(high_pos),trans)+' '+ units[ukeys[k+1]]+ ' '
                    num = str(int(num)%ukeys[k+1])
                    
            # When we reach here, we need to determine the positions of the last
            # two digits. If the last digit is zero, do not add 'zero' to the 
            # end of the number. If the penultimate digit is greater than 1, then
            # resolve the digits individually, else look up the value in the 'low'
            # dictionary
            
            if (((int(num)//100) < 1) and (int(num) !=0)):
            
                if num in low.keys() :
                    trans +=low[num]
                    return trans
                else :
                    high_pos = int(num)//10
                    trans += ties[str(high_pos)]
                    num = str(int(num)%10)
                    
            
        return trans


while True:
    try:
        i= raw_input("Please enter an integer to be displayed: ")
        i=int(i)
    except ValueError:
        print("Please enter a valid integer.")
        continue
    else:
        break

print("Number {} is {}".format(i,conv(i)))
    
    


