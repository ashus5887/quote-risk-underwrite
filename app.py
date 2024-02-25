import os
from flask import Flask, jsonify, request
from src import risk_assess_model

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    age = float(request.args.get('age'))
    yoj = float(request.args.get('yoj'))
    income = str(request.args.get('income'))
    travtime = int(request.args.get('travtime'))
    caruse = str(request.args.get('caruse'))
    bluebook = str(request.args.get('bluebook'))
    cartype = str(request.args.get('cartype'))
    redcar = str(request.args.get('redcar'))
    carage = float(request.args.get('carage'))
    urbanicity = str(request.args.get('urbanicity'))
    mvrpts = int(request.args.get('mvrpts'))
    X_input = [[age, yoj, income, travtime, caruse, bluebook, cartype, redcar, mvrpts, carage, urbanicity]]
    risk_score = risk_assess_model.get_risk_factor(X_input)
    return jsonify({'risk_score': risk_score})

if __name__ == '__main__':
    # Use the PORT environment variable provided by Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
