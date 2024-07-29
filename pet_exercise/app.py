import json

from flask import Flask, request, render_template, redirect, url_for

from pet_exercise.cat import Cat
from pet_exercise.dog import Dog
from pet_exercise.owner import Owner
from pet_exercise.pet import Pet

app = Flask(__name__)

owners = []
pets = []


@app.route('/')
def home():
    return render_template('home.html')


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
        owner = next((o for o in owners if o.name == owner_name), None)
        if owner:
            if species == 'Dog':
                breed = request.form['breed']
                pet = Dog(name, age, owner, breed)
            elif species == 'Cat':
                indoor = request.form.get('indoor') == 'on'
                pet = Cat(name, age, owner, indoor)
            owner.add_pet(pet)
            pets.append(pet)
        return redirect(url_for('list_pets'))
    return render_template('add_pet.html', owners=owners)


@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)
