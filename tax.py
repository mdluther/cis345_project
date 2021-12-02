from dataclasses import dataclass


@dataclass
class Tax:
    tax_code: str
    description: str
    tax_type: str
    exemptions: list()

    def __repr__(self):
        return f"Code: {self.tax_code}\nDescription: {self.description}\nType: {self.tax_type}\nExemptions: {self.exemptions}"
