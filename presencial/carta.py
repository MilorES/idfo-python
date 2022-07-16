from datetime import datetime
from articulo import Articulo


class Carta:
    # Carta, Camareros, Cocinero, Aforo, Mesas, Horario
    def __init__(self):
        self._articulos = {
                    "Primeros":[
                                Articulo("Paella",10.9),
                                Articulo("Ensalada",8.3)
                            ],
                    "Segundos":[
                        Articulo("Estofado",12.2),
                        Articulo("Lentejas",13.0)
                            ],
                    "Postres":[
                        Articulo("Flan",4.2),
                        Articulo("Helado",3.0)
                            ]        
                    }
        self.fecha_actualizada = datetime.today()
    
    def mostrar(self):
        for categoria, articulos in self._articulos.items():
            print(categoria)
            for articulo in articulos:
                print(articulo)
