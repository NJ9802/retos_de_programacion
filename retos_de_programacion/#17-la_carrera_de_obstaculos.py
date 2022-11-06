# /*
#  * Reto #17
#  * LA CARRERA DE OBSTÁCULOS
#  * Fecha publicación enunciado: 25/04/22
#  * Fecha publicación resolución: 02/05/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#  *        variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

class Atleta:
    def __init__(self, actions:str) -> None:
        self.actions = actions.lower().split()

def race(atleta, track):

    list_track = list(track)
    if len(atleta.actions) >= len(list_track):
        total_actions = len(list_track)
    else:
        total_actions = len(atleta.actions)
    
    result = []

    for index in range(total_actions):
        
        if atleta.actions[index] == 'run':
            if list_track[index] == '_':
                result.append(list_track[index])
            else:
                result.append('/')
        
        else:
            if list_track[index] == '_':
                result.append('x')
            else:
                result.append(list_track[index]) 
    
    if result == list_track:
        print(''.join(result))
        return True
    else:
        print(''.join(result))
        return False

atleta1 = Atleta('run jump jump run run')

tracks = ('_|__|', '|__|___', '_||__', '|_|', '___|__|', '_||_|', '|_______')

spaces = ''

for index, track in enumerate(tracks, 1):
    if race(atleta1, track):
        print(f'{spaces:<8}Race {index:^5} Success!')

    else:
        print(f'{spaces:<8}Race {index:^5} Fails')

