class Country:
    def __init__(self, country_code, name, taxes=None):
        self.__country_code = country_code
        self.__name = name
        self.taxes = taxes if taxes else []

    def __str__(self):
        return f"\nCountry Code: {self.country_code}\nName: {self.name}\nTaxes:{''.join(map(str, self.taxes))}\n"

    @property
    def country_code(self):
        return self.__country_code.upper()

    @country_code.setter
    def country_code(self, country_code):
        self.__country_code = country_code.upper()

    @property
    def name(self):
        return self.__name.upper()

    @name.setter
    def name(self, name):
        self.__name = name.upper()

    @property
    def taxes(self):
        return self.__taxes

    @taxes.setter
    def taxes(self, taxes):
        self.__taxes = taxes
