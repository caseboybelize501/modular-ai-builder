from flask import Flask, render_template
import os
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    slots = scan_feeder_slots()
    recipes = load_recipes()
    return render_template('index.html', slots=slots, recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)

# Helper functions

def scan_feeder_slots():
    # Implement feeder slot scanning logic here
    pass

def load_recipes():
    recipes = {}
    for filename in os.listdir('recipes'):
        if filename.endswith('.yaml'):
            with open(os.path.join('recipes', filename), 'r') as file:
                recipes[filename] = yaml.safe_load(file)
    return recipes
