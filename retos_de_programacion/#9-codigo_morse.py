# /*
#  * Reto #9
#  * CÓDIGO MORSE
#  * Fecha publicación enunciado: 02/03/22
#  * Fecha publicación resolución: 07/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#%%
import re
# CH == '~'
code = { 
'A' : '·— ',     'N' : '—· ', 	  	'0': 	'————— ',
'B' : '—··· ',   'Ñ' : '——·—— ', 	  	'1' :	'· ———— ',
'C' : '—·—· ',	'O' : '——— ', 	  	'2': 	'··——— ',
'~': '———— ',	'P' : '·——· ', 	  	'3' :	'···—— ',
'D' : '—·· ',	'Q' : '——·— ', 	  	'4': 	'····— ',
'E' : '· ',	  	'R' : '·—· ', 	  	'5': 	'····· ',
'F' : '··—· ',	'S' :	'··· ', 	  	'6': 	'—···· ',
'G' : '——· ',	  	'T': 	'— ', 	  	'7': 	'——··· ',
'H' : '···· ',	  	'U': 	'··— ', 	  	'8': 	'———·· ',
'I' : '·· ',	  	'V': 	'···— ', 	  	'9': 	'————· ',
'J' : '·——— ',	  	'W': 	'·—— ', 	  	'.': 	'·—·—·— ',
'K' : '—·— ',  	'X' :	'—··— ', 	  	',' :	'——··—— ',
'L' : '·—·· ', 	  	'Y': 	'—·—— ', 	  	'?': 	'··——·· ',
'M' : '—— ', 	  	'Z': 	'——·· ', 	  	'"': 	'·—··—· ',
'/' :	'—··—· ', ' ': '   ',
}

reverse_code = {morse : letter for letter, morse in code.items()}
reverse_code['———— '] = 'CH'


def traducir(string):
    if re.match(r'\w', string):
        
        iter_string = re.sub('CH', '~', string.upper())
        
        
        for letter in iter_string:
            if letter == ' ':
                continue

            iter_string = iter_string.replace(letter, code[letter])

        iter_string = re.sub('  ', '   ', iter_string)
            
            
        return iter_string

    else:
        iter_string = re.sub('  ', ' * ', string).split()
        
        
        for index, letter in enumerate(iter_string):
            if letter == '*':
                iter_string[index] = ' '
            else:
                iter_string[index] = reverse_code[f'{letter} ']
        
        return ''.join(iter_string).capitalize()

print(traducir('···· ——— ·—·· ·— ——··——   —— ·   ·—·· ·—·· ·— —— ———   ·——· · ·—· ··· ——— —·   —·——   —— ·   ——· ··— ··· — ·—   ·—·· ·—   ·—·· · ———— ·   —·· ·   ···— ·— —·—· ·— ·—·—·—'))
print(traducir('Hola, me llamo PERSON y me gusta la leche de vaca.'))
#%%

     