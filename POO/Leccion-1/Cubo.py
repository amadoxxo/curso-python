class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    
    def volumen_cubo(self):
        return self.ancho * self.alto * self.profundo


ancho = int(input('Ingrese el ancho del cubo: '))
alto = int(input('Ingrese el alto del cubo: '))
profundo = int(input('Ingrese lo profundo del cubo: '))

cubo1 = Cubo(ancho, alto, profundo)

print(f'El volumen del cubo es de: {cubo1.volumen_cubo()}')