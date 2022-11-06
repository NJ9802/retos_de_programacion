def is_narcisist(number):
    if number <= 0:
        return False

    len_number = len(str(number))
    total = 0
    
    for digit in str(number):
        total += int(digit)**len_number

    if total == number:
        return True

    else:
        return False

for number in range(1000000):
    if is_narcisist(number):
        print(number) 