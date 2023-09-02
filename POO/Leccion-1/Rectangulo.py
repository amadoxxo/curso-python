class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

base = int(input('Ingrese la base del rectángulo: '))
altura = int(input('Ingrese la altura del rectángulo: '))

rectangulo1 = Rectangulo(base,altura)
print(f'El area del rectangulo es de: {rectangulo1.area()}')

base = int(input('Ingrese la base del rectángulo: '))
altura = int(input('Ingrese la altura del rectángulo: '))

rectangulo2 = Rectangulo(base,altura)
print(f'El area del rectangulo es de: {rectangulo2.area()}')