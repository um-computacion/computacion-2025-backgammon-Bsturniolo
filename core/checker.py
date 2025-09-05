class checker:

    def __init__(self, owner: int):
        self.__owner__ = owner

    def __repr__(self):
        return f"checker({self.__owner__})"