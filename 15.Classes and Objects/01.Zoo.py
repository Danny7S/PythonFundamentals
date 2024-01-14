class Zoo:
    _animals = 0

    def __init__(self, zoo_name: str):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.species = species
        self.name = name
        if self.species == 'mammal':
            self.mammals.append(self.name)
        elif self.species == 'fish':
            self.fishes.append(self.name)
        elif self.species == 'bird':
            self.birds.append(self.name)
        self._animals += 1

    def get_info(self, species):
        if species == 'mammal':
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {self._animals}")
        elif species == 'fish':
            print(f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {self._animals}")
        elif species == 'bird':
            print(f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {self._animals}")


our_zoo_name = input()
zoo1 = Zoo(our_zoo_name)
num_of_anim = int(input())

for i in range(num_of_anim):
    animal_type, animal_name = input().split()
    zoo1.add_animal(animal_type, animal_name)

searched_type = input()
zoo1.get_info(searched_type)
