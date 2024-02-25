import os
from flask import Flask, request, jsonify
from src import risk_assess_model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict(age, yoj, income, travtime, caruse, bluebook, cartype, redcar, carage, urbanicity, mvrpts):
    X_input = [[age, yoj, income, travtime, caruse, bluebook, cartype, redcar, carage, urbanicity, mvrpts]]
    risk_score = risk_assess_model.get_risk_factor(X_input)
    return jsonify({'risk_score': risk_score})

if __name__ == '__main__':
    # Use the PORT environment variable provided by Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
