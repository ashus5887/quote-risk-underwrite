import os

import pandas as pd
from src.utils import data_prep

def prep_data(path:str):
    data = data_prep.clean_data(path, ['INCOME', 'HOME_VAL', 'OLDCLAIM', 'CLM_AMT', 'BLUEBOOK'])
    df = pd.DataFrame(data, columns=['KIDSDRIV', 'AGE', 'HOMEKIDS', 'YOJ', 'INCOME', 'PARENT1', 'HOME_VAL', 'MSTATUS', 'GENDER', 'EDUCATION', 'OCCUPATION', 'TRAVTIME', 'CAR_USE', 'BLUEBOOK', 'TIF', 'CAR_TYPE', 'RED_CAR', 'OLDCLAIM', 'CLM_FREQ', 'REVOKED', 'MVR_PTS', 'CLM_AMT', 'CAR_AGE', 'URBANICITY', 'CLAIM_FLAG'])
    data_prep.encode_categorical_data(df, df, df)
    return df

def assess_correlation():
    current_dir = os.getcwd()
    folder = os.path.abspath(os.path.join(current_dir, '..', '..'))
    file_name = 'raw_dataset.csv'
    file_path = os.path.join(folder, file_name)
    df = prep_data(file_path)
    correlation = df.corr()['CLAIM_FLAG'].sort_values(ascending=False)
    # Print column names with correlation values
    for column, corr_value in correlation.items():
        print(f"{column}: {corr_value}")

if __name__ == "__main__":
    assess_correlation()
