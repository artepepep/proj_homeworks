class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    def add(self, oc):
        new_country = f'{self.name} {oc.name}'
        new_population = self.population + oc.population
        bosnia_1 = Country(new_country, new_population)
        return bosnia_1
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)