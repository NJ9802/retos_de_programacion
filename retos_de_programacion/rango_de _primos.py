import sys



def is_primo(number):

    if number <= 1:
        return False

    for i in range(2,number):
        if number % i == 0:
            return False
        
        
    return True

if len(sys.argv) == 2:
    try:    
        arg = (int(sys.argv[1]))
    except:
        print('Argument must be number')
else: 
    print('The program works with 1 argument')

for y in range(2,arg):
    if is_primo(y):
        print(y)
    
                
           
    
        


    