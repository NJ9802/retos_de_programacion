import sys

def is_primo(number):

    for i in range(2,11):
        
        if not i == number:
            
            if number % i == 0:
                return print("isn't primo")
    
    return print('is primo')
                
           
    
        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:    
            is_primo(int(sys.argv[1]))
        except:
            print('Argument must be number')
    else: 
        print('The program works with 1 argument')