import matplotlib.pyplot as plt
import pandas as pd

def imprimeavg(grouped_regions,region,type_c_o):
    '''
    Prints a graph with the average price during de 4 years.
    '''
    df_years=grouped_regions.loc[region,type_c_o]
    plt.bar(df_years.index,df_years['AveragePrice'])
    plt.title('{} Conventional Avocados'.format(region), fontsize=16, fontweight=0, color='Red')
    plt.xlabel("Years")
    plt.ylabel("Average Price")
    plt.savefig('../output/averageprice{}.png'.format(region))

    return

def imprimetot(grouped_regions,region,type_c_o):
    '''
    Prints a graph with total volume each year.
    '''
    df_years=grouped_regions.loc[region,type_c_o]
    plt.bar(df_years.index,df_years['Total Volume'])
    plt.title('{} Conventional Avocados'.format(region), fontsize=16, fontweight=0, color='Red')
    plt.xlabel("Years")
    plt.ylabel("Total Volume")
    plt.savefig('../output/totalvolume{}.png'.format(region))
    return


