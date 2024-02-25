import os
from flask import Flask, jsonify, request
from src import risk_assess_model
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    age = float(request.args.get('age'))
    yoj = float(request.args.get('yoj'))
    income = str(unquote(request.args.get('income')))
    travtime = int(request.args.get('travtime'))
    caruse = str(request.args.get('caruse'))
    bluebook = str(unquote(request.args.get('bluebook')))
    cartype = str(request.args.get('cartype'))
    redcar = str(request.args.get('redcar'))
    mvrpts = int(request.args.get('mvrpts'))
    carage = float(request.args.get('carage'))
    urbanicity = str(request.args.get('urbanicity'))
    X_input = [[age, yoj, income, travtime, caruse, bluebook, cartype, redcar, mvrpts, carage, urbanicity]]
    risk_score = risk_assess_model.get_risk_factor(X_input)
    return jsonify({'risk_score': risk_score})

if __name__ == '__main__':
    # Use the PORT environment variable provided by Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
