from dataclasses import dataclass


@dataclass
class Tax:
    tax_code: str
    name: str
    tax_type: str
    exemptions: list()
