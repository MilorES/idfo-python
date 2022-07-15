import sys # Para que funcione la entrada de parametros
import math

# Type Hint
def iniciar_proceso(carga_electrica:int, numero_ciclos:int) -> int:
    return 23 * carga_electrica // numero_ciclos

def crear_informe(res_proceso:int) -> str:
    #dato_validacion = resultado_proceso ** 2
    dato_validacion = math.pow(res_proceso,2)
    return f"{dato_validacion}"

# Programa Principal
if __name__ == "__main__":
    print(sys.argv[0]) # path con el programa
    # Recogida de argumentos o valor
    if len(sys.argv) == 3:
        carga = int(sys.argv[1])
        ciclos = int(sys.argv[2])
        resultado_proceso = iniciar_proceso(carga,ciclos) # Invocación
        print(f"El proceso ha finalizado con un score {resultado_proceso}")
        print(crear_informe(resultado_proceso))
    else:
        print("ERROR: Número de parametros erroneos")

