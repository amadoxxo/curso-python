class Persona:
    contador_persona = 0
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona
    
    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'{self.id_persona} {self.nombre} {self.edad}'

persona1 = Persona('Elian', 21)
persona2 = Persona('Camila', 19)
persona3 = Persona('Mafe', 18)
Persona.generar_siguiente_valor()
persona4 = Persona('Carolina', 21)
print(persona1)
print(persona2)
print(persona3)
print(persona4)
print(f'Valor contador personas: {Persona.contador_persona}')