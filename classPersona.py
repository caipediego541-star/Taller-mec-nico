class Persona:
    #atritubuto
    def __init__(self,nombre,dni,contacto):
        #encapsulamineto con _ Esto vuelve el atributo protegido.
        self._nombre=nombre
        #encapsulamiento con __ Esto hace el atributo privado.
        self.__dni=dni
        #encapsulamiento con __ Esto hace el atributo privado.
        self.__contacto=contacto
    #metodos y encapsulamiento para hacerlos privados.
    # Investiga y Arreglar
    @property
    def dni(self):
        return self.__dni
    def mostrar_datos(self):
        return f"Nombre: {self._nombre}, DNI: {self.dni}, teléfono {self.__contacto}"
    def identificarse(self):
        return f"Mi nombre es {self._nombre} con DNI {self.dni}"
#clase hija mecanico.
class Mecanico:
    def __init__(self,nombre,dni,contacto):
        #atributos. Agregar a los atributos encapsulamiento.
        self.nombre=nombre
        self.dni=dni
        self.contacto=contacto
    def mostrar_datos(self):
        return f"Mecanico: {self.nombre} con DNI {self.dni}, contacto {self.contacto}"
class Cliente:
    def __init__(self,nombre,dni,contacto):
        #atributos. Agregar a los atributos encapsulamiento.
        self.nombre=nombre
        self.dni=dni
        self.contacto=contacto
    def mostrar_datos(self):
        return f"Cliente {self.nombre} con DNI {self.dni} y contacto {self.contacto}"
    