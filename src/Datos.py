import cleaning

def getDatos(fecha,region):
    df=cleaning.cleaningColumns()
    datos=[]
    r=df[(df.Date==fecha) & (df.region==region) & (df.type=='conventional')]
    datos.append(r['AveragePrice'].item())
    datos.append(r['Total Volume'].item())
    print(datos)
    return datos