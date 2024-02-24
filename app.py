from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    # Get input features from request
    data = request.json
    KIDSDRIV = data['KIDSDRIV']
    AGE = data['AGE']
    HOMEKIDS = data['HOMEKIDS']
    YOJ = data['YOJ']
    INCOME = data['INCOME']
    PARENT1 = data['PARENT1']
    HOME_VAL = data['HOME_VAL']
    MSTATUS = data['MSTATUS']
    GENDER = data['GENDER']
    EDUCATION = data['EDUCATION']
    OCCUPATION = data['OCCUPATION']
    TRAVTIME = data['TRAVTIME']
    CAR_USE = data['CAR_USE']
    BLUEBOOK = data['BLUEBOOK']
    TIF = data['TIF']
    CAR_TYPE = data['CAR_TYPE']
    RED_CAR = data['RED_CAR']
    OLDCLAIM = data['OLDCLAIM']
    CLM_FREQ = data['CLM_FREQ']
    REVOKED = data['REVOKED']
    MVR_PTS = data['MVR_PTS']
    CLM_AMT = data['CLM_AMT']
    CAR_AGE = data['CAR_AGE']
    URBANICITY = data['URBANICITY']

    # Call the predict_risk method of RiskPredictor class
    risk_score = predict_risk(KIDSDRIV, AGE, HOMEKIDS, YOJ, INCOME, PARENT1, HOME_VAL, MSTATUS, GENDER, EDUCATION, OCCUPATION, TRAVTIME, CAR_USE, BLUEBOOK, TIF, CAR_TYPE, RED_CAR, OLDCLAIM, CLM_FREQ, REVOKED, MVR_PTS, CLM_AMT, CAR_AGE, URBANICITY)

    # Return the output as JSON
    return jsonify({'risk_score': risk_score})

def predict_risk(self, KIDSDRIV, AGE, HOMEKIDS, YOJ, INCOME, PARENT1, HOME_VAL, MSTATUS, GENDER, EDUCATION, OCCUPATION, TRAVTIME, CAR_USE, BLUEBOOK, TIF, CAR_TYPE, RED_CAR, OLDCLAIM, CLM_FREQ, REVOKED, MVR_PTS, CLM_AMT, CAR_AGE, URBANICITY):
    return 0.0
    # yet to implement
    # model = joblib.load('trained_model.pkl')

if __name__ == '__main__':
    app.run()
