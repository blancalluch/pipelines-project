import cleaning
import pandas as pd
import pdf

def getDatos(year,region,type_c_o):
    '''
    Merges the avocado dataset and the supermarket addresses read from the 
    googlemaps API.
    '''
    avocados=cleaning.cleaningColumns()

    supermarkets=datosDeApi()

    df_merged=pd.merge(avocados, supermarkets, how='outer', on=['region'])

    grouped_regions=cleaning.groupingData(df_merged)
    
    gr=grouped_regions.loc[region,type_c_o,int(year)]
    data=[]

    #average price
    data.append(gr[0])
    #total volume
    data.append(gr[1])
    #Address
    data.append(gr[2])
    #super market
    data.append(gr[3])
    #print(data)
    #imprimir graficas
    pdf.creaPDF(grouped_regions,year,region,type_c_o,data)
    #plotting.imprimeavg(grouped_regions,region,type_c_o)
    #plotting.imprimetot(grouped_regions,region,type_c_o)
    return data

def datosDeApi():
    '''
    Reads the dataset created with the information from the googlemaps API.
    '''
    supermarket=pd.read_csv('../output/Region_supermarket.csv')
    return supermarket