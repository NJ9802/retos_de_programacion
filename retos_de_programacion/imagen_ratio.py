#
#  Reto #5
#  ASPECT RATIO DE UNA IMAGEN
#  Fecha publicación enunciados: 01/02/22
#  Fecha publicación resolución: 07/02/22
#  Dificultad: DIFÍCIL
#
#  Enunciado: Crea un programa que se encargue de calcular y el aspect ratio de una imagen a partir de una url.
#  - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1921080px.
#
#  Información adicional:
#  - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar
#    ayuda la comunidad.
#  - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#



from PIL import Image
import urllib.request
from math import gcd

url = "data:image/png;base64,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"



def download_image(url_image: str):
    filename = 'image'+'.png'
    urllib.request.urlretrieve(url, filename)

def open_image():
    image = Image.open('image.png')
    width, height = image.size
    return width, height

# greatest common factor (GCF or GCD or HCF)
def calculation_GCF(width, height):
    width_int = int(width)
    height_int = int(height)
    return width_int, height_int, gcd(width_int, height_int)
    

def aspect_ratio(width, heigth, hcd):
    first= int(width/hcd)
    second=int(heigth/hcd)   
    
    print("\n ******************************** RUN **********************************")
    print(f"The ASPECT RATIO of the image of width {width}px and heigth {heigth}px is: {first}:{second}")


# ---------------------------------- run ---------------------------------- #
image_downloaded=download_image(url)

width, heigth = open_image()
aspect_ratio(*calculation_GCF(width,heigth))      

# -------------------------------------- test ----------------------------------
# width=640
# heigth=480 
# calculation_GCF(width, heigth)  
# aspect_ratio(*calculation_GCF(width,heigth))     # Escribe un archivo IMAGE_NAME.
