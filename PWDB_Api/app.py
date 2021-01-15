import flask 
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
wrestlingcompanys = [
    {'id': 0,
     'company': 'WWE',
     'owner': 'Vince McMahon',
     'year_created': '1953'},
    {'id': 1,
     'company': 'AEW',
     'owner': 'Tony Kahn',
     'year_created': '2019'},
    {'id': 2,
     'company': 'Impact! Wrestling',
     'owner': 'Anthem Sports & Entertainment/Dixie Carter',
     'year_created': '2002'},
    {'id': 3,
     'company': 'NWA',
     'owner': 'Billy Corgan',
     'year_created': '1948'},
    {'id': 4,
     'company': 'MLW',
     'owner': 'Court Bauer',
     'year_created': '2002'},
    {'id': 5,
     'company': 'NJPW',
     'owner': 'Bushiroad/TV Asahi/Amuse, Inc.',
     'year_created': '1972'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/wrestlingcompany/all', methods=['GET'])
def api_all():
    return jsonify(wrestlingcompany)

@app.route('/api/v1/resources/wrestlingcompanys', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for wrestlingcompany in wrestlingcompanys:
        if wrestlingcompany['id'] == id:
            results.append(wrestlingcompany)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()

