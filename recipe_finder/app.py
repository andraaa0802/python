from flask import Flask, render_template, request, redirect, url_for
import requests
import random

app = Flask(__name__)

SPOONACULAR_API_KEY = 'your_spoonacular_api_key_here'

# Define a list of possible random search terms
RANDOM_SEARCH_TERMS = ["pasta", "salad", "soup", "dessert", "vegetarian", "chicken"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])

def search_recipes():
    try:
        if request.method == 'POST':
            search_query = request.form.get('query')
            api_url = f'https://api.spoonacular.com/recipes/search?apiKey={SPOONACULAR_API_KEY}&query={search_query}'

            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if response.status_code == 200:
                recipes = data.get('results', [])
                return render_template('results.html', recipes=recipes)
            else:
                return render_template('error.html', error=data.get('message', 'Unknown error'))

        elif request.method == 'GET':
            # Handle the GET request for the /search route if needed
            return render_template('index.html')

    except requests.exceptions.RequestException as e:
        app.logger.error(f'Error during recipe search: {e}')
        return render_template('error.html', error='An error occurred while processing your request.')

@app.route('/recipe/<int:recipe_id>')
def recipe_details(recipe_id):
    try:
        api_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={SPOONACULAR_API_KEY}'

        response = requests.get(api_url)
        response.raise_for_status()
        recipe_data = response.json()

        if response.status_code == 200:
            return render_template('recipe_details.html', recipe=recipe_data)
        else:
            return render_template('error.html', error=recipe_data.get('message', 'Unknown error'))

    except requests.exceptions.RequestException as e:
        app.logger.error(f'Error retrieving recipe details: {e}')
        return render_template('error.html', error='An error occurred while retrieving recipe details.')

@app.route('/feeling_lucky', methods=['GET'])
def feeling_lucky():
    try:
        # List of possible search terms
        possible_search_terms = ['chicken', 'pasta', 'vegetarian', 'dessert', 'soup']

        # Generate a random search term
        random_search_term = random.choice(possible_search_terms)

        # Redirect to the search route with the random search term
        return redirect(url_for('search_recipes', query=random_search_term))

    except Exception as e:
        app.logger.error(f'Error during "I\'m Feeling Lucky" operation: {e}')
        return render_template('error.html', error='An error occurred while processing your request.')
if __name__ == '__main__':
    app.run(debug=True)
