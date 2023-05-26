
import pandas as pd

import pipeline_data

def test_pipeline_mediane():
    
    df = pd.DataFrame({
        'age': [1, 2, 3],
        'temperature': [4, -1, 2]
    })
    
    result = pipeline_data.median_mean_pipeline(df)
    assert isinstance(result, pd.DataFrame)
    assert len(result.columns) == len(df.columns)
    
    df2 = pd.DataFrame({
        'X1': [1, 1, 1],
        'X2': [1, 1, 1]
    })
    
    result = pipeline_data.median_mean_pipeline(df2)
    assert result['X1'].tolist() == [0]