from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for recipes
recipes = [
    {
        'id': 1,
        'title': 'Spaghetti Carbonara',
        'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'],
        'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'
    },
    {
        'id': 2,
        'title': 'Tomato Soup',
        'ingredients': ['tomato', 'water', 'salt'],
        'instructions': 'Boil all together until mushy, blend, and serve.'
    },
    {
        'id': 3,
        'title': 'Grilled Cheese Sandwich',
        'ingredients': ['bread', 'cheese', 'butter'],
        'instructions': 'Butter bread, place cheese between slices, grill until golden.'
    }
]

# Endpoint to get a single recipe by its ID
@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe), 200
    else:
        return jsonify({'error': 'Recipe not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
