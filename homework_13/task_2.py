class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    def __add__(self, other):
        if isinstance(other, Country):
            new_country_name = f'{self.name} {other.name}'
            new_country_population = self.population + other.population
            new_country = Country(new_country_name, new_country_population)
            return new_country
        else:
            raise TypeError("error")
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)