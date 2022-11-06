import sys

def decimal_to_binary(number):
    x = number
    binary = []

    while x > 0:
        rest = x % 2
        x //= 2

        binary.append(str(rest))

    return ''.join(binary)

if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        if int(sys.argv[1]) > 0:
            try:
                print(f'The number {sys.argv[1]} is {decimal_to_binary(int(sys.argv[1]))} in binary')
            except:
                print('Argument must be a number!')
                sys.exit(1)
        else:
            print('The number must be positive')
            sys.exit(1)            

    else:
        print('Enter 1 number as argument without spaces')
        sys.exit(1)