from flask import Flask
from helper import pets

app = Flask(__name__)

app.debug = True

@app.route('/')
@app.route('/home')
def index():
    return """<h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href="/animals/dogs">Dogs</a></li>
        <li><a href="/animals/cats">Cats</a></li>
        <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    """



@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"<h1> List of {pet_type}</h1>"
    html += "<ul>"

    index = 0

    for pet in pets[pet_type]:
        name = pet["name"]
        # looping through and displaying correct index for each link of pet in animal type
        html += f"""
        <li><a href="/animals/{pet_type}/{index}">{name}</a></li>
        """
        # updating to current index of each animal 
        index += 1

    html += "</ul>"
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    pet_name = pet["name"]
    pet_img = pet["url"]
    pet_description = pet["description"]
    pet_breed = pet["breed"]
    pet_age = pet["age"]
    html = f"""
    <h1>{pet_name}</h1>
    <img alt="image of pet breed: {pet_breed}" src="{pet_img}">
    <p>{pet_description}</p>
    <ul>
        <li> Age: {pet_age}</li>
        <li> Breed: {pet_breed}</li>
    </ul>
    <a href="/">Return Home</a>
    """
    return html



