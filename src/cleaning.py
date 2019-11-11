import pandas as pd
import re

def cleaningColumns():
    dataf = pd.read_csv('../input/avocado.csv', encoding = "cp1252") 
    df=dataf.drop(['4046','4225','4770','Total Bags', 
        'Small Bags', 'Large Bags', 'XLarge Bags'],axis=1)
    df=df.rename(columns={'Unnamed: 0': 'id'})
    data=renamingRegions(df)
    return data

def renamingRegions(avocado):
    lr=avocado['region'].copy()
    for r in range(len(lr)):
        palabras=re.findall('[A-Z][^A-Z]*', lr[r])
        lr[r]=" ".join(palabras)
        avocado['region']=list(lr)
        avocado.loc[(avocado["region"]=='West Tex New Mexico'), "region"] = 'New Mexico'
    return avocado


