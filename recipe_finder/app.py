from flask import Flask, render_template, request, redirect, url_for
import requests
import random

app = Flask(__name__)

SPOONACULAR_API_KEY = 'd8167a83add04d1c913b7a6d25f87cc7'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_recipes():
    try:
        search_query = request.form.get('query')
        api_url = f'https://api.spoonacular.com/recipes/search?apiKey={SPOONACULAR_API_KEY}&query={search_query}'

        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200:
            recipes = data.get('results', [])
            return render_template('results.html', recipes=recipes,search_term=search_query)
        else:
            return render_template('error.html', error=data.get('message', 'Unknown error'))

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

@app.route('/feeling_lucky', methods=[ 'POST'])
def feeling_lucky():
    try:
        predefined_queries = ["Pasta", "Chicken", "Salad", "Dessert", "Vegetarian", "Brownie", "Pizza", "Christmas", "Egg", "Chocolate", "Cheese", "Olive"]

        random_query = random.choice(predefined_queries)

        api_url = f'https://api.spoonacular.com/recipes/search?apiKey={SPOONACULAR_API_KEY}&query={random_query}'

        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200:
            recipes = data.get('results', [])
            return render_template('results.html', recipes=recipes, search_term=random_query)
        else:
            return render_template('error.html', error=data.get('message', 'Unknown error'))

    except requests.exceptions.RequestException as e:
        app.logger.error(f'Error during lucky recipe retrieval: {e}')
        return render_template('error.html', error='An error occurred while processing your request.')

if __name__ == '__main__':
    app.run(debug=True)
