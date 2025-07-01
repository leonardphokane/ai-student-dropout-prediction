import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df = df.fillna(method='ffill')
    df = pd.get_dummies(df, columns=['language', 'location'])
    scaler = StandardScaler()
    df[['time_spent', 'quiz_score']] = scaler.fit_transform(df[['time_spent', 'quiz_score']])
    return df
