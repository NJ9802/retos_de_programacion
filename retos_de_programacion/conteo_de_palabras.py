import re
import sys

def word_count(string):
    string_list = re.split(r'\W+', string.lower())
    keys_list = set(string_list)

    
    for key in keys_list:
        if key:
            count_of_words = string_list.count(key)
            print(f'There are {count_of_words} "{key}" in the sentence')



if __name__ == '__main__':
    if len(sys.argv) == 2:
        word_count(sys.argv[1])
    
    elif len(sys.argv) > 2:
        print("You must enter the sentence between 'quotes'")

    else:
        print('Enter a sentence between "quotes" as an argument')
