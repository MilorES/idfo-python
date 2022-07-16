from mailbox import NoSuchMailboxError


class Articulo:

    def __init__(self, nombre, precio) -> None:
        self._nombre = nombre
        self._precio = precio

    def __str__(self) -> str:
        return f"{self._nombre} {self._precio}"
