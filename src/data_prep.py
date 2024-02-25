import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler, LabelEncoder


def clean_data(path:str, columns:list):
    data = pd.read_csv(path)

    # Clean the data
    # Remove the $ symbol
    cols = columns
    for col in cols:
        data[col] = data[col].str.replace(',', '').str.replace('$', '').astype('float')

    # Remove '_z' attached to the data
    for col in data.columns:
        if(data[col].dtype == "object"):
            data[col] = data[col].str.replace('z_', '')

    # Fill empty values
    data.fillna(data.mode().iloc[0], inplace=True)

    return data

def scale_numeric_data(X:pd.DataFrame, X_train:pd.DataFrame, X_test:pd.DataFrame):
    numeric_features = []
    for col in X.columns:
        if(X[col].dtype == "float" or X[col].dtype == "int"):
            numeric_features.append(col)
    scaler = StandardScaler()
    X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
    X_test[numeric_features] = scaler.fit_transform(X_test[numeric_features])

def encode_categorical_data(X:pd.DataFrame, X_train:pd.DataFrame, X_test:pd.DataFrame):
    categorical_features = X.select_dtypes(include=['object']).columns
    encoder = LabelEncoder()
    for col in categorical_features:
        X_train[col] = encoder.fit_transform(X_train[col])
        X_test[col] = encoder.fit_transform(X_test[col])

def undersample_data(X_train:pd.DataFrame, X_test:pd.DataFrame, y_train:pd.DataFrame, y_test:pd.DataFrame):
    undersample = RandomUnderSampler(sampling_strategy='majority')
    X_train_resampled, y_train_resampled = undersample.fit_resample(X_train, y_train)
    X_test_resampled, y_test_resampled = undersample.fit_resample(X_test, y_test)

    return X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled