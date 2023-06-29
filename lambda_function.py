import pandas as pd
def lambda_handler(event, context):
    d = {'Column1': [1,2], 'column2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1')
