from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from populate_db import Fighter  # Ensure Fighter has an `id` column

# Set up Flask
app = Flask(__name__)

# Connect to the database
engine = create_engine('sqlite:///fighter_stats.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to classify fighters by weight
def get_weight_class(weight):
    if weight is None:  # Handle cases where weight might be missing
        return "Unknown"
    try:
        weight = float(weight)  # Ensure weight is a float for comparison
    except ValueError:
        return "Unknown"  # If weight cannot be converted to a number

    # Categorize by weight class (in kilograms)
    if weight <= 56.7:
        return "Flyweight"
    elif weight > 56.7 and weight <= 61.2:
        return "Bantamweight"
    elif weight > 61.2 and weight <= 65.8:
        return "Featherweight"
    elif weight > 65.8 and weight <= 70.3:
        return "Lightweight"
    elif weight > 70.3 and weight <= 77.1:
        return "Welterweight"
    elif weight > 77.1 and weight <= 83.9:
        return "Middleweight"
    elif weight > 83.9 and weight <= 93.0:
        return "Light Heavyweight"
    else:
        return "Heavyweight"




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fighters', methods=['GET'])
def get_fighters():
    # Query all fighters from the database
    fighters = session.query(Fighter).all()
    data = [
        {
            "id": fighter.id,
            "name": fighter.name,
            "wins": fighter.wins,
            "losses": fighter.losses,
            "height": fighter.height,
            "weight": fighter.weight,
            "reach": fighter.reach,
            "stance": fighter.stance,
            "age": fighter.age,
            "SLpM": fighter.SLpM,
            "sig_str_acc": fighter.sig_str_acc,
            "SApM": fighter.SApM,
            "str_def": fighter.str_def,
            "td_avg": fighter.td_avg,
            "td_acc": fighter.td_acc,
            "td_def": fighter.td_def,
            "sub_avg": fighter.sub_avg,
            "performance_score": fighter.performance_score,
            "weight_class": get_weight_class(fighter.weight),  # Add weight class
        }
        for fighter in fighters
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
