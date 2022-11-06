import re

def capitalize_text(string):
    words_list = re.findall(r'[A-z]+', string)
    sentence = string
    for word in words_list:
        sentence = re.sub(word, word.capitalize(), sentence)
    
    return sentence

print(capitalize_text('que hacen Por alla'))
