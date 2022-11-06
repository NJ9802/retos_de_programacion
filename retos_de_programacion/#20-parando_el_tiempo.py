# /*
#  * Reto #20
#  * PARANDO EL TIEMPO
#  * Fecha publicación enunciado: 16/05/22
#  * Fecha publicación resolución: 23/05/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

import asyncio
import time

async def async_sum(a, b, seconds):
    
    init_time = time.time()
    
    result = a + b 
    
    await asyncio.sleep(seconds)
    
    print(f'{a} + {b} = {result}')
    
    final_time = time.time()
    
    print(f'Task completed in {round(final_time - init_time,2)} seconds!')

async def main():

    init_time = time.time()
    
    await asyncio.gather( 
        async_sum(5, 6, 3),
        async_sum(3, 0, 5),
        async_sum(4, 74, 9),
        async_sum(5, 5, 7),
        async_sum(2, 2, 2),
        async_sum(1, 1, 1),
        async_sum(2, 3, 5)
    )
    
    final_time = time.time()

    print('----------------------')
    print(f'Main task completed in {final_time - init_time} seconds')

if __name__ == '__main__':
    asyncio.run(main())