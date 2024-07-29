from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from pet_exercise.pet import Pet


class Owner:

    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self._pets: List['Pet'] = []

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    @name.setter
    def name(self, name):
        try:
            self._name = name
        except TypeError as e:
            print(e)

    @phone_number.setter
    def phone_number(self, phone):
        try:
            self._phone_number = phone
        except TypeError as e:
            print(e)

    def get_owner_pets(self):
        return self._pets

    def add_pet(self, pet: 'Pet'):
        try:
            self._pets.append(pet)
        except TypeError as e:
            print(e)

    def remove_pet(self, pet: 'Pet'):
        try:
            if pet in self._pets:
                self._pets.remove(pet)
            else:
                print("owner dont have this pet")
        except TypeError as e:
            print(e)

    def __str__(self):
        pets_str = ', '.join([str(pet) for pet in self._pets])
        return f"{self.name}: {pets_str}"
