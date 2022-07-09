from array import array
class Propietario:
    @property
    def nombre(self):
        return self._nombre

    def __init__(self, nombre):
        self._nombre = nombre

class Semaforo:
    def __init__(self,color="Amarillo"):
        self._color = color

    @property #getter
    def color(self):
        return self._color

    @color.setter
    def color(self,nuevo_color:str):
        self._color = nuevo_color

class Coche:
    def __init__(self,marca:str, 
                modelo:str = None, 
                color:str = None, 
                cilindrada:str = None,
                propietario:Propietario = None):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindrada = cilindrada
        self.propietario:str = propietario

    def arranca_motor(self):
        print(f" {self.propietario.nombre} arrancando el {self.marca} {self.modelo}")

def cargar_coches_en_carrera(*coches,l_carrera:array):
    for coche in coches:
        l_carrera.append(coche)

if __name__ == "__main__":
    # Instanciar Clase -> Objeto
    coche_jose = Coche("SEAT","Ibiza","Rojo","1200",Propietario("Jose Antonio Rojo"))
    coche_alba = Coche("SEAT","Ibiza","Azul","1800",Propietario("Alba Lorca"))
    coche_josefa = Coche("Citroen","Xsara","Granate","1500",Propietario("Josefa González"))

    semaforo_salida = Semaforo("Verde")

    a_coches = [coche_jose, coche_alba, coche_josefa] 
    print("*" * 60)
    for coche in a_coches:
        coche.arranca_motor()

# objeto carrera    

'''
Crear una funcion que arranque todos los coches de una carrera
Carrera es un ARRAY de obetos de tipo Coche
'''