from flask import Flask, request, jsonify
from jsonschema import validate

app = Flask(__name__)

# start data, used to test the GET function
movies = [
    {'id': 1, 'title': 'Gladiator', 'genre': 'Action', 'would_watch_again': True, 'personal_rating': 10,
     'would_recommend': True},
    {'id': 2, 'title': 'Titanic', 'genre': 'Drama', 'would_watch_again': True, 'personal_rating': 10,
     'would_recommend': True},
    {'id': 3, 'title': 'Dead Poets Society', 'genre': 'Drama', 'would_watch_again': True, 'personal_rating': 9,
     'would_recommend': True}
]

# explicit schema definition
movie_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "genre": {"type": "string"},
        "would_watch_again": {"type": "boolean"},
        "personal_rating": {"type": "integer"},
        "would_recommend": {"type": "boolean"}
    },
    "required": ["title", "genre", "personal_rating"]
}


# Endpoint to get the list of all movies in JSON format
@app.route('/movies', methods=['GET'])
def get_all_movies():
    return jsonify({'movies': movies})


# Endpoint to add a new movie. Validation present to ensure the schema defined above is followed
@app.route('/movies', methods=['POST'])
def add_movie():
    movie_data = request.get_json()

    try:
        validate(instance=movie_data, schema=movie_schema)
    except Exception as e:
        return jsonify({'error': 'Invalid request data. ' + str(e)}), 400

    new_movie = {
        'id': len(movies) + 1,
        'title': movie_data['title'],
        'genre': movie_data['genre'],
        'would_watch_again': movie_data.get('would_watch_again', False),
        'personal_rating': movie_data['personal_rating'],
        'would_recommend': movie_data.get('would_watch_again', False)
    }

    movies.append(new_movie)

    return jsonify({'movie': new_movie}), 201



# run the python file

if __name__ == '__main__':
    app.run(debug=True)