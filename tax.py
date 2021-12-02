from dataclasses import dataclass


@dataclass
class Tax:
    tax_code: str
    description: str
    tax_type: str
    exemptions: list()

    def __repr__(self):
        return f"\n\tCode: {self.tax_code}\n\tDescription: {self.description}\n\tType: {self.tax_type}\n\tExemptions: {self.exemptions}\n"
