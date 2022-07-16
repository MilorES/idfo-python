from cocinero import Cocinero
from carta import Carta
from restaurante import Restaurante


if __name__ == "__main__":
    # Crear Restaurante
    res_pdp = Restaurante("Pont de Princep","972504550",Carta(),100,None)
    print(res_pdp)
    # Crear Cocinero
    chef = Cocinero("40495452X","Paco",53,12)
    res_pdp.contratar_cocinero(chef)
    res_pdp.mostrar_carta()
    