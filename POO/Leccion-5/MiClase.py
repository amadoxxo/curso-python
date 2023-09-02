class MiClase:
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
        
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
    
    
MiClase.metodo_clase()
miObjeto1 = MiClase('variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

# miClase1 = MiClase('Esta es una variable de instancia') 
# miClase2 = MiClase('Nueva variable de instancia')

# MiClase.variable_clase2 = 'Variable al vuelo'

# print(MiClase.variable_clase)
# print(miClase1.variable_instancia)
# print(miClase1.variable_clase)
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)

# # Variable al vuelo
# print(MiClase.variable_clase2)
# print(miClase1.variable_clase2)
# print(miClase2.variable_clase2)
