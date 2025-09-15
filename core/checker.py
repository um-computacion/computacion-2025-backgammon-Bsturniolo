class checker:
    def __init__(self, owner: int):
        self.__owner__ = owner

    def __repr__(self):
        return f"checker({self.__owner__})"

    def get_owner(self):
        """Devuelve el propietario de la ficha (1 o -1)."""
        return self.__owner__
