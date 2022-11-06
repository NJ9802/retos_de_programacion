import sys

class Polygon:
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth

    def area(self):
        return self.base * self.heigth

    def print_area(self):
        return print(f'El area es: {self.area()}')


class Triangle(Polygon): 
        
    def area(self):
        return (self.base * self.heigth) / 2
        
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    pass
    

def get_area(polygon):
    """
    This function return the area of one given polygon,
    to run this script you must insert 3 arguments.

    Example: Type_of_polygon base heigth
    
    Polygons admitted: Triangle, Square, Rectangle

    PD: In square case you must give only the base argument
    """
    polygon.print_area()

if __name__ == '__main__':
    
    args = sys.argv

    if len(args) == 1:
        print('To know how this script works give it "doc" argument')
        sys.exit(0)
    
    if args[1].lower() == 'doc':
        print(get_area.__doc__)
        sys.exit(0)

    polygon = args[1].lower()
    len_args = len(args)
    
    if len_args > 2:
        try:
            base = int(args[2])
        
            if polygon != 'square':
                heigth = int(args[3])
        
        except:
            print('Arguments next to the type of polygon must be numbers')
            sys.exit(1)
        
    if polygon == 'square':
        
        if len_args == 3:
            get_area(Square(base))
        
        else: 
            print('Square only need 1 argument')
    
    elif polygon == 'triangle':

        if len_args == 4:
            get_area(Triangle(base, heigth))
        else:
            print('Triangle needs 2 arguments (base and heigth)')

    elif polygon == 'rectangle':

        if len_args == 4:
            get_area(Rectangle(base, heigth))
        else:
            print('Rectangle needs 2 arguments (base and heigth)')

    else:
        print("""Arguments must be 'Type of polygon, base and heigth'
polygons admitted: Square, Triangle, Rectangle""")
        sys.exit(1)
