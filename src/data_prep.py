import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler, LabelEncoder


def clean_data(path:str, currency_columns:list):
    data = pd.read_csv(path)

    # Clean the data
    # Remove the $ symbol
    cols = currency_columns
    for col in cols:
        data[col] = data[col].str.replace(',', '').str.replace('$', '').astype('float')

    # Remove '_z' attached to the data
    for col in data.columns:
        if(data[col].dtype == "object"):
            data[col] = data[col].str.replace('z_', '')

    # Fill empty values
    data.fillna(data.mode().iloc[0], inplace=True)

    return data

def encode_categorical_data(path:str):
    data = pd.read_csv(path)

    car_type_map = {'Minivan': 0, 'Panel Truck': 1, 'Pickup': 2, 'Sports Car': 3, 'SUV': 4, 'Van': 5}
    red_car_map = {'yes': 0, 'no': 1}
    urbanicity_map = {'Highly Rural/ Rural': 0, 'Highly Urban/ Urban': 1}
    car_use_map = {'Private': 0, 'Commercial': 1}

    data['CAR_TYPE'] = data['CAR_TYPE'].map(car_type_map)
    data['RED_CAR'] = data['RED_CAR'].map(red_car_map)
    data['URBANICITY'] = data['URBANICITY'].map(urbanicity_map)
    data['CAR_USE'] = data['CAR_USE'].map(car_use_map)

    return data

def scale_numeric_data(X:pd.DataFrame, X_train:pd.DataFrame, X_test:pd.DataFrame):
    numeric_features = []
    for col in X.columns:
        if(X[col].dtype == "float" or X[col].dtype == "int"):
            numeric_features.append(col)
    scaler = StandardScaler()
    X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
    X_test[numeric_features] = scaler.fit_transform(X_test[numeric_features])


def undersample_data(X_train:pd.DataFrame, X_test:pd.DataFrame, y_train:pd.DataFrame, y_test:pd.DataFrame):
    undersample = RandomUnderSampler(sampling_strategy='majority')
    X_train_resampled, y_train_resampled = undersample.fit_resample(X_train, y_train)
    X_test_resampled, y_test_resampled = undersample.fit_resample(X_test, y_test)

    return X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled