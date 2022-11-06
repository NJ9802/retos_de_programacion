
#%%
from collections import deque

def check(string):
    pairs = {'{':'}', '[':']', '(':')',}
    reverse_pairs = {value: key for key, value in pairs.items()}
    opens = deque()
    
    for letter in string:
        if letter in pairs.keys():
            opens.append(letter)

        elif letter in pairs.values() and reverse_pairs[letter] == opens[-1]:
            opens.pop()

        elif letter in pairs.values():
            return f'String "{string}" is not balanced'

    
    if opens:
        return f'String "{string}" is not balanced'             
    else:
        return f'String "{string}" is balanced'
    
        

print(check('{5*(6+8)}'))
print(check('{5*](6+8)}'))
print(check('a{s({5f*[(){}]6d+8)}'))

print(check('a{s({5f*[(){}]6}d+8)}'))

#%%