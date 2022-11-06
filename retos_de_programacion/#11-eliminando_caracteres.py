# %%

def characters_delete(str1, str2):
    
    output1 = set(str1.lower()) - set(str2.lower())
    output2 = set(str2.lower()) - set(str1.lower())
        
    print(''.join(output1))
    print(''.join(output2))


characters_delete('abcdefghijklmn', 'la vaca lola tiene cabeza y tiene cola')

# %%