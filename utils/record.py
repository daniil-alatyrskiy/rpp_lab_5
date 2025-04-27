class Record:
    allowed_attrs = {'№', 'ФИО', 'должность', 'трудовой стаж'}

    def __validate_value(self, attr_name, value):
        match attr_name:
            case "№":
                if int(value) < 1:
                    raise ValueError("Number must be positive")
            case "трудовой стаж":
                if not (0 < int(value) < 90):
                    raise ValueError("Experience should be real")
            case _:
                pass

    def __init__(self, number, fio, position, experience):
        self.__setattr__('№', number)
        self.__setattr__('ФИО', fio)
        self.__setattr__('должность', position)
        self.__setattr__('трудовой стаж', experience)

    def __setattr__(self, name, value):
        try:
            if name in self.allowed_attrs:
                self.__validate_value(name, value)
                object.__setattr__(self, name, value)
            else:
                raise AttributeError(f"Нельзя установить неизвестный атрибут '{name}'")
        except Exception as exp:
            raise ValueError(f"Try to fix your csv file, there is an Exception with {name}: {str(exp)}")

    def __repr__(self):
        data = self.__dict__
        return (f"Record(№={data['№']}, ФИО='{data['ФИО']}', "
                f"должность='{data['должность']}', трудовой стаж={data['трудовой стаж']})")
