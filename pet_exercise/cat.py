from pet_exercise.enum.pet_species import PetSpecies
from pet_exercise.pet import Pet


class Cat(Pet):

    def __init__(self, name, age, owner, indoor):
        super().__init__(name, age, PetSpecies.CATS.value, owner)
        self.indoor = indoor

    @property
    def indoor(self):
        return self._indoor

    @indoor.setter
    def indoor(self, indoor: bool):
        try:
            self._indoor = indoor
        except TypeError as e:
            print(e)

    def is_living_indoor(self):
        if self._indoor:
            return "the cat lives indoor"
        else:
            return "the cat lives outside"

    def move_out_side(self):
        if self._indoor:
            self._indoor = False
        else:
            return "the cat lives outside the house"

    def __str__(self):
        owner_name = self.owner
        vaccinated = self.pet_is_vaccinated()
        return f"{self.name} (Cat:{self.age} years old, Owner: {owner_name}, {vaccinated} )"
