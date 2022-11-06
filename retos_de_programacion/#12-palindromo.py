# %%

import re, string

def remove_punctuation_and_spaces ( text ):
  return re.sub('[%s]' % re.escape(string.punctuation), '', re.sub(r"\s+", "", text))

def are_palindrome(text):

    text_modified = remove_punctuation_and_spaces(text)
    

    if list(text_modified.lower()) == list(text_modified.lower())[::-1]:
        return True
    
    else:
        return False

words = ('Ana, lleva al oso la avellana.','Adivina ya te opina, ya ni miles origona, ya ni cetro me domina','ola','Ana, ana', 'olrtlo', 'olla allo')

for word in words:
    if are_palindrome(word):
        print(word)
#%%