import pandas as pd
from src import data_prep

def prep_data(path:str):
    data = data_prep.clean_data(path, ['INCOME', 'HOME_VAL', 'OLDCLAIM', 'CLM_AMT', 'BLUEBOOK'], ['CAR_USE', 'CAR_TYPE', 'RED_CAR', 'URBANICITY'])
    df = pd.DataFrame(data, columns=['KIDSDRIV', 'AGE', 'HOMEKIDS', 'YOJ', 'INCOME', 'PARENT1', 'HOME_VAL', 'MSTATUS', 'GENDER', 'EDUCATION', 'OCCUPATION', 'TRAVTIME', 'CAR_USE', 'BLUEBOOK', 'TIF', 'CAR_TYPE', 'RED_CAR', 'OLDCLAIM', 'CLM_FREQ', 'REVOKED', 'MVR_PTS', 'CLM_AMT', 'CAR_AGE', 'URBANICITY', 'CLAIM_FLAG'])
    data_prep.encode_categorical_data(df, df, df)
    return df

def assess_correlation():
    df = prep_data("../data/raw_dataset.csv")
    correlation = df.corr()['CLAIM_FLAG'].sort_values(ascending=False)
    # Print column names with correlation values
    for column, corr_value in correlation.items():
        print(f"{column}: {corr_value}")

if __name__ == "__main__":
    assess_correlation()
