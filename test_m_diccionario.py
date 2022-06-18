import m_diccionario as m_dict

def pintar_separador():
    print("-" * 60)

nuevo_diccionario = {}
m_dict.diccionario_alta("Pedro","18",nuevo_diccionario)
m_dict.diccionario_alta("Juan","31",nuevo_diccionario)
pintar_separador()
m_dict.diccionario_recorrer(nuevo_diccionario)
m_dict.diccionario_baja("Pedro",nuevo_diccionario)
pintar_separador()
m_dict.diccionario_recorrer(nuevo_diccionario)
m_dict.diccionario_actualizar("Juan","77",nuevo_diccionario)
pintar_separador()
m_dict.diccionario_recorrer(nuevo_diccionario)
