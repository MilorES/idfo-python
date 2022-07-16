from cocinero import Cocinero
from carta import Carta

class Restaurante:
    # Carta, Camareros, Cocinero, Aforo, Mesas, Horario
    def __init__(self, nombre, telefono, carta:Carta, aforo:int, mesas) -> None:
        self._nombre = nombre
        self._carta = carta
        self._telefono = telefono
        self._camareros = list()
        self._cocineros = list()
        self._aforo = aforo
        self._mesas = mesas
        self._horario = "12 a 18"

    def __str__(self) -> str:
        return f"{self._nombre} {self._telefono} {self._telefono} {self._aforo}"

    def contratar_cocinero(self, cocinero):
        self._cocineros.append(cocinero)
        print(f"El chef {cocinero.nombre} ha sido contratado")

    def mostrar_carta(self):
        self._carta.mostrar()