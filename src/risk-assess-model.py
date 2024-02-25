import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from src import data_prep

def prep_data(path:str):
    data = pd.read_csv(path)
    X = data[['AGE', 'YOJ', 'INCOME', 'TRAVTIME', 'CAR_USE', 'BLUEBOOK', 'CAR_TYPE', 'RED_CAR', 'CAR_AGE', 'URBANICITY', 'MVR_PTS']]
    y = data['RISK_VALUE']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12, shuffle=True)
    data_prep.scale_numeric_data(X, X_train, X_test)
    data_prep.encode_categorical_data(X, X_train, X_test)
    X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled = data_prep.undersample_data(X_train, X_test, y_train, y_test)
    return X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled

def log_reg(X_train_resampled, y_train_resampled):
    model = LogisticRegression(max_iter=500)
    model.fit(X_train_resampled, y_train_resampled)
    return model

def train_model(path:str):
    X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled = prep_data(path)
    model = log_reg(X_train_resampled, y_train_resampled)

    # Test Model
    y_pred = model.predict(X_test_resampled)

    # Evaluate the model
    accuracy = accuracy_score(y_test_resampled, y_pred)
    print("Accuracy:", accuracy)

    # Additional evaluation metrics
    print("Classification Report:")
    print(classification_report(y_test_resampled, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test_resampled, y_pred))
    return model

if __name__ == "__main__":
    model = train_model("../data/final_dataset.csv")



# # Convert to probabilities
# probs = model.predict_proba(X_test)[:, 1]
#
# # Rescale probabilities to range from 1 to 10
# risk_scores = (probs * 2) + 1
#
# # Convert risk_scores to integer values
# risk_scores = np.round(risk_scores).astype(int)
# result_df = pd.DataFrame({'Risk_Score': risk_scores})