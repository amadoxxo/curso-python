# Ejemplo atributos publicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido, privado) -> None:
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objeto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')
# Acceso al atributo público
print(objeto.publico)
# Modificar el valor publico
objeto.publico = 'Nuevo valor publico'
print(objeto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
print(objeto._protegido)
# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

# Acceder al valor privado
# print(objeto.__privado)
# Pero, convierte: objeto._clase__atributo_privado
print(objeto._MiClase__privado)
# Modificar valor privado
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)
