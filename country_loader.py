import json
from tax import Tax
from country import Country


def load_countries(filepath):
    try:
        with open(filepath) as file:
            country_data = json.load(file)
    except (FileNotFoundError):
        print("Country data file not found. No countries have been loaded.")
        return []

    countries = {}

    for country_code, country_properties in country_data.items():
        countries[country_code] = Country(
            country_code,
            country_properties[0],
            {
                tax_code: Tax(
                    tax_code, tax_properties[0], tax_properties[1], tax_properties[2]
                )
                for tax_code, tax_properties in country_properties[1].items()
            },
        )

    return countries
