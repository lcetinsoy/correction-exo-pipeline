import pandas as pd

def median_mean_pipeline(df: pd.DataFrame):

    data = {}
    for column in df.columns:
        data[column] = df[column].mean() - df[column].median()
    
    result = pd.DataFrame(data, index=[0])
    return result