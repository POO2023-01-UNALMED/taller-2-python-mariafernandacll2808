class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        numAsientos = 0
        for a in self.asientos:
            if isinstance(a, Asiento):
                numAsientos += 1
        return numAsientos
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for a in self.asientos:
            if a != None:
                if a.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"
    
class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color = color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self,registro):
        self.registro = registro   

    def asignarTipo(self,tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

            