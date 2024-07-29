import json
from flask import Flask, request, render_template, redirect, url_for
from pet_exercise.src.classes.cat import Cat
from pet_exercise.src.classes.dog import Dog
from pet_exercise.src.classes.owner import Owner
import os

app = Flask(__name__)

owners = []
pets = []


def save_owners(filename='owners.json'):
    with open(filename, 'w') as file:
        json.dump([owner.to_dict() for owner in owners], file)


def save_pets(filename='pets.json'):
    with open(filename, 'w') as file:
        json.dump([pet.to_dict() for pet in pets], file)


def load_owners(filename='owners.json'):
    global owners
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                owners_data = json.load(file)
                if isinstance(owners_data, list):
                    owners = [Owner.from_dict(owner_data) for owner_data in owners_data]
                else:
                    print(f"Error: Expected a list of owners, got {type(owners_data)}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading owners data: {e}")
    else:
        print(f"{filename} not found. No owners data loaded.")


def load_pets(filename='pets.json'):
    global pets
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                pets_data = json.load(file)
                for pet_data in pets_data:
                    owner = next((o for o in owners if o.name == pet_data['owner_name']), None)
                    if owner:
                        if pet_data['species'] == 'Dog':
                            pet = Dog.from_dict(pet_data, owner)
                        elif pet_data['species'] == 'Cat':
                            pet = Cat.from_dict(pet_data, owner)
                        pets.append(pet)
                        owner.add_pet(pet)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading pets data: {e}")
    else:
        print(f"{filename} not found. No pets data loaded.")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/owners')
def list_owners():
    return render_template('owners.html', owners=owners)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        owner = Owner(name, phone_number)
        owners.append(owner)
        save_owners()
        return redirect(url_for('list_owners'))
    return render_template('add_owner.html')


@app.route('/pets')
def list_pets():
    return render_template('pets.html', pets=pets)


@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = int(request.form['age'])
        owner_name = request.form['owner']
        vaccinated = request.form.get('vaccinated') == 'on'
        owner = next((o for o in owners if o.name == owner_name), None)
        if owner:
            if species == 'Dog':
                breed = request.form['breed']
                pet = Dog(name, age, owner, breed, vaccinated)
            elif species == 'Cat':
                indoor = request.form.get('indoor') == 'on'
                pet = Cat(name, age, owner, indoor, vaccinated)

            owner.add_pet(pet)
            pets.append(pet)
            save_pets()
        return redirect(url_for('list_pets'))
    return render_template('add_pet.html', owners=owners)


@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    load_owners()
    load_pets()
    app.run(debug=True)
