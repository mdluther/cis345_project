from tax import *
import json

with open("country_data.json") as file:
    country_data = json.load(file)


class Country:
    def __init__(self, country_code, name, taxes=None):
        self.__country_code = country_code
        self.__name = name

        if not taxes:
            self.__taxes = [
                Tax(tax_code, *tax)
                for values in country_data.values()
                for tax in values[1:]
                for tax_code, tax in tax.items()
            ]

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
        return [tax for tax in self.__taxes]
