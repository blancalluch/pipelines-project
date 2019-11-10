import pandas as pd

def cleaningDatos():
    dataf = pd.read_csv('./INPUT/avocado.csv', encoding = "cp1252") 
    df=dataf.drop(['4046','4225','4770','Total Bags', 
        'Small Bags', 'Large Bags', 'XLarge Bags'],axis=1)
    return df

