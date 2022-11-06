# /*
#  * Reto #19
#  * CONVERSOR TIEMPO
#  * Fecha publicación enunciado: 09/05/22
#  * Fecha publicación resolución: 16/05/22
#  * Dificultad: FACIL
#  *
#  * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */


#%%
def time_conversor(day=0, hours=0, min=0, seconds=0):
    day_miliseconds = day * 60 * 60 * 24 * 1000
    hours_miliseconds = hours * 60 * 60 * 1000
    min_miliseconds = min * 60 * 1000
    seconds_miliseconds = seconds * 1000
    miliseconds = day_miliseconds + hours_miliseconds + min_miliseconds + seconds_miliseconds

    return f'There are {miliseconds} miliseconds'

print(time_conversor(day=2, min=-50 , seconds=50))

#%%