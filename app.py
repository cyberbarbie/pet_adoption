from flask import Flask
from helper import pets

app = Flask(__name__)

app.debug = True

@app.route('/')
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

    for pet in pets[pet_type]:
        name = pet["name"]
        html += f"<li>{name}</li>"

    html += "</ul>"
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return pet



