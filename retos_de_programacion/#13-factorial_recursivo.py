

def factorial_recursivo(number):
    if number == 1:
        # print('*******************')
        # print('number == 1')
        # print(number)
        # print('*******************')
        return 1

    else:
        # print('-----------------------')
        # print(f'number: {number}')
        # print(f'fac: {factorial_recursivo(number-1)}')
        # print(f'product: {number * factorial_recursivo(number-1)}')
        # print('-------------------------------')
        return number * factorial_recursivo(number-1)

print(factorial_recursivo(5))