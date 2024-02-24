import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.under_sampling import RandomUnderSampler
from xgboost.testing.data import joblib

# Read the dataset
data = pd.read_csv("../data/car_insurance_claim.csv")

# Clean the data
# Remove the $ symbol
cols = ['INCOME', 'HOME_VAL', 'OLDCLAIM', 'CLM_AMT', 'BLUEBOOK']
for col in cols:
    data[col] = data[col].str.replace(',', '').str.replace('$', '').astype('float')

# Remove '_z' attached to the data
for col in data.columns:
    if(data[col].dtype == "object"):
        data[col] = data[col].str.replace('z_', '')

# Fill empty values
data.fillna(data.mode().iloc[0], inplace=True)

# Split data
X = data[['KIDSDRIV', 'AGE', 'HOMEKIDS', 'YOJ', 'INCOME', 'PARENT1', 'HOME_VAL', 'MSTATUS', 'GENDER', 'EDUCATION', 'OCCUPATION', 'TRAVTIME', 'CAR_USE', 'BLUEBOOK', 'TIF', 'CAR_TYPE', 'RED_CAR', 'OLDCLAIM', 'CLM_FREQ', 'REVOKED', 'MVR_PTS', 'CLM_AMT', 'CAR_AGE', 'URBANICITY']]
y = data['CLAIM_FLAG']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12, shuffle=True)

# Scaling the numeric features
numeric_features = []
for col in X.columns:
    if(X[col].dtype == "float" or X[col].dtype == "int"):
        numeric_features.append(col)
scaler = StandardScaler()
X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
X_test[numeric_features] = scaler.fit_transform(X_test[numeric_features])

# Encoding the categorical features
categorical_features = X.select_dtypes(include=['object']).columns
encoder = LabelEncoder()
for col in categorical_features:
    X_train[col] = encoder.fit_transform(X_train[col])
    X_test[col] = encoder.fit_transform(X_test[col])

# undersampling the data
undersample = RandomUnderSampler(sampling_strategy='majority')
X_train_resampled, y_train_resampled = undersample.fit_resample(X_train, y_train)
X_test_resampled, y_test_resampled = undersample.fit_resample(X_test, y_test)

# LOGISTIC REGRESSION
# Initialize and fit the logistic regression model
model = LogisticRegression(max_iter=50)
model.fit(X_train_resampled, y_train_resampled)
joblib.dump(model, 'trained_model.pkl')


# Convert to probabilities
probs = model.predict_proba(X_test)[:, 1]

# Rescale probabilities to range from 1 to 10
risk_scores = (probs * 2) + 1

# Convert risk_scores to integer values
risk_scores = np.round(risk_scores).astype(int)
result_df = pd.DataFrame({'Risk_Score': risk_scores})