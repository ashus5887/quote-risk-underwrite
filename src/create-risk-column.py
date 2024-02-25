import pandas as pd
from src import data_prep

def calculate_risk_age(age, risk):
    if age > 15 and age <= 25:
        risk += 1
    elif age > 40 and age <= 55:
        risk += 1
    elif age > 55 and age <= 65:
        risk += 2
    elif age > 65:
        risk += 3
    else:
        risk += 0
    # Add more conditions as needed
    return risk

def calculate_risk_yoj(yoj, risk):
    if yoj > 0 and yoj <= 5:
        risk += 2
    elif yoj > 5 and yoj <= 10:
        risk += 1
    else:
        risk += 0
    return risk

def calculate_risk_income(income, risk):
    if income <= 50000:
        risk += 0
    elif 50000 < income <= 100000:
        risk += 1
    elif 100000 < income <= 250000:
        risk += 2
    elif income > 250000:
        risk += 3
    else:
        risk += 0
    return risk

def calculate_risk_travtime(travtime, risk):
    if travtime <= 35:
        risk += 0
    elif 35 < travtime <= 70:
        risk += 1
    elif 70 < travtime <= 105:
        risk += 2
    elif travtime > 105:
        risk += 3
    else:
        risk += 0
    return risk

def calculate_risk_caruse(caruse, risk):
    if caruse == 'Commercial':
        risk += 1
    else:
        risk += 0
    return risk

def calculate_risk_carprice(car_price, risk):
    if car_price <= 10000:
        risk += 0
    elif 10000 < car_price <= 30000:
        risk += 1
    elif 30000 < car_price <= 50000:
        risk += 2
    else:
        risk += 3
    return risk

def calculate_risk_cartype(car_type, risk):
    if car_type == "Minivan":
        risk += 2
    elif car_type == "Panel Truck":
        risk += 3
    elif car_type == "Pickup":
        risk += 3
    elif car_type == "Sports Car":
        risk += 4
    elif car_type == "SUV":
        risk += 3
    elif car_type == "Van":
        risk += 2
    else:
        risk += 0
    return risk

def calculate_risk_redcar(redcar, risk):
    if redcar == "yes":
        risk += 1
    else:
        risk += 0
    return risk

def calculate_risk_carage(carage, risk):
    if carage <= 5:
        risk += 1
    elif 5 > carage <= 10:
        risk += 2
    elif 10 > carage <= 15:
        risk += 3
    elif carage > 15:
        risk += 4
    else:
        risk += 0
    return risk

def calculate_risk_isurban(isurban, risk):
    if isurban == 'Highly Urban/ Urban':
        risk += 1
    else:
        risk += 0
    return risk

def calculate_risk_mvrpoints(mvrpoints, risk):
    if mvrpoints <= 3:
        risk += 1
    elif mvrpoints <= 6:
        risk += 2
    elif mvrpoints <= 10:
        risk += 3
    else:
        risk += 4
    return risk


if __name__ == "__main__":
    data = data_prep.clean_data("../data/raw_dataset.csv", ['INCOME', 'HOME_VAL', 'OLDCLAIM', 'CLM_AMT', 'BLUEBOOK'])
    df = pd.DataFrame(data)
    columns_to_drop = ['ID', 'KIDSDRIV', 'BIRTH', 'HOMEKIDS', 'PARENT1', 'HOME_VAL', 'MSTATUS', 'GENDER', 'EDUCATION', 'OCCUPATION', 'TIF', 'OLDCLAIM', 'CLM_FREQ', 'REVOKED', 'CLM_AMT', 'CLAIM_FLAG']
    df.drop(columns=columns_to_drop, inplace=True)
    risk_values = []
    for index, row in df.iterrows():
        risk = 0
        age = row['AGE']
        risk = calculate_risk_age(age, risk)
        yoj = row['YOJ']
        risk = calculate_risk_yoj(yoj, risk)
        income = row['INCOME']
        risk = calculate_risk_income(income, risk)
        travtime = row['TRAVTIME']
        risk = calculate_risk_travtime(travtime, risk)
        caruse = row['CAR_USE']
        risk = calculate_risk_caruse(caruse, risk)
        carprice = row ['BLUEBOOK']
        risk = calculate_risk_carprice(carprice, risk)
        cartype = row['CAR_TYPE']
        risk = calculate_risk_cartype(cartype, risk)
        redcar = row['RED_CAR']
        risk = calculate_risk_redcar(redcar, risk)
        carage = row['CAR_AGE']
        risk = calculate_risk_carage(carage, risk)
        isurban = row['URBANICITY']
        risk = calculate_risk_isurban(isurban, risk)
        mvrpoints = row['MVR_PTS']
        risk = calculate_risk_mvrpoints(mvrpoints, risk)
        risk = int((risk/2) + 1)
        risk_values.append(risk)

    # Add risk values as a new column to the DataFrame
    df['RISK_VALUE'] = risk_values
    folder_path = '../data/'
    # Display the updated DataFrame
    df.to_csv(folder_path + 'final_dataset.csv', index=False)

