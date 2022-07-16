from persona import Persona


class Cocinero(Persona):
    pass
    def __init__(self, dni, nombre, edad, experiencia) -> None:
        super().__init__(dni, nombre, edad)
        self._experiencia = experiencia

    @property
    def experiencia(self):
        return self._experiencia
