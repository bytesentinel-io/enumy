class Enumy:
    def __init__(self, allowed_values: tuple = None, allowed_type: type = None) -> None:
        self.__allowed_values = allowed_values
        self.__allowed_type = allowed_type
        self.__value = None

    def __repr__(self) -> None:
        return self.__value
    
    def set(self, value) -> None:
        if type(value) != self.__allowed_type:
            raise ValueError(f"Invalid value for {self.__class__.__name__}. The value must be of type {self.__allowed_type}.")
        elif value is None or value not in self.__allowed_values:
            raise ValueError(f"Invalid value for {self.__class__.__name__}. The value must be one of the following: {self.__allowed_values}")
        else:
            self.__value = value

    def get(self) -> None:
        return self.__value

    def check_type(self, type: type) -> bool:
        if type is self.__allowed_type:
            return True
        else:
            return False
    
    def check(self, value, type: type) -> bool:
        if type(value) == type:
            return True
        else:
            return False

    def check_value(self, value) -> bool:
        if value in self.__allowed_values:
            return True
        else:
            return False