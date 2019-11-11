import pandas as pd
import re

def cleaningColumns():
    '''
    Removes columns that aren't required for the study.
    '''
    dataf = pd.read_csv('../input/avocado.csv', encoding = "cp1252") 
    df=dataf.drop(['4046','4225','4770','Total Bags', 
        'Small Bags', 'Large Bags', 'XLarge Bags','Unnamed: 0'],axis=1)
    #df=df.rename(columns={'Unnamed: 0': 'id'})
    data=renamingRegions(df)
    return data

def renamingRegions(avo):
    '''
    Renames the regions by adding spaces in them.
    '''
    lr=avo['region'].copy()
    regionList=[]
    for r in range(len(lr)):
        palabras=re.findall('[A-Z][^A-Z]*', lr[r])
        regionList.append(" ".join(palabras))
    avo['region']=regionList
    avo.loc[(avo["region"]=='West Tex New Mexico'), "region"] = 'New Mexico'
    return avo


def groupingData(df):
    '''
    Groups the weeks of each year with the corresponding region and type of avocado.
    '''
    grouped_data=df.groupby(['region','type','year']).agg({'AveragePrice': 'mean', 'Total Volume': 'mean','Address': 'min', 'Supermarket Name':'min'})
    return grouped_data




