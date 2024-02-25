from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from src import data_prep


def prep_data(path: str):
    data = data_prep.encode_categorical_data(path)
    X = data[['AGE', 'YOJ', 'INCOME', 'TRAVTIME', 'CAR_USE', 'BLUEBOOK', 'CAR_TYPE', 'RED_CAR', 'CAR_AGE', 'URBANICITY',
              'MVR_PTS']]
    y = data['RISK_VALUE']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12, shuffle=True)
    # data_prep.scale_numeric_data(X, X_train, X_test)
    # X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled = data_prep.undersample_data(X_train,
                                                                            # X_test,y_train,y_test)
    return X_train, X_test, y_train, y_test


def linear_reg(X_train_resampled, y_train_resampled):
    model = LinearRegression()
    model.fit(X_train_resampled, y_train_resampled)

    return model


def train_model(path: str):
    X_train_resampled, X_test_resampled, y_train_resampled, y_test_resampled = prep_data(path)
    model = linear_reg(X_train_resampled, y_train_resampled)

    return model


def get_risk_factor(X_input):
    model = train_model("../data/final_dataset.csv")

    currency_values = [2, 5]
    for val in currency_values:
        X_input[0][val] = float(X_input[0][val].replace(',', '').replace('$', ''))

    if (X_input[0][4] == 'Private'):
        X_input[0][4] = 0
    elif (X_input[0][4] == 'Commercial'):
        X_input[0][4] = 1
    else:
        X_input[0][4] = 2

    if (X_input[0][6] == 'Minivan'):
        X_input[0][6] = 0
    elif (X_input[0][6] == 'Panel Truck'):
        X_input[0][6] = 1
    elif (X_input[0][6] == 'Pickup'):
        X_input[0][6] = 2
    elif (X_input[0][6] == 'Sports Car'):
        X_input[0][6] = 3
    elif (X_input[0][6] == 'SUV'):
        X_input[0][6] = 4
    elif (X_input[0][6] == 'Van'):
        X_input[0][6] = 5
    else:
        X_input[0][6] = 6

    if (X_input[0][7] == 'yes'):
        X_input[0][7] = 0
    elif (X_input[0][7] == 'no'):
        X_input[0][7] = 1
    else:
        X_input[0][7] = 2

    if (X_input[0][10] == 'Highly Rural/ Rural'):
        X_input[0][10] = 0
    elif (X_input[0][10] == 'Highly Urban/ Urban'):
        X_input[0][10] = 1
    else:
        X_input[0][10] = 2

    risk_factor = model.predict(X_input)
    risk_factor = 10 if risk_factor >= 10 else risk_factor
    return int(risk_factor)


# if __name__ == '__main__':
#     # X = [[46.0, 12.0, '$43,501', 60, 'Private', '$16,080', 'Minivan', 'no', 2, 1.0, 'Highly Rural/ Rural']]
#     X = [[60.0, 50.0, '$10,000', 20, 'Private', '$5,000', 'Van', 'yes', 1, 10.0, 'Highly Urban/ Urban']]
#     print(get_risk_factor(X))
