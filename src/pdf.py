import plotting

def creaPDF(grouped_regions,region,type_c_o):

    
    plotting.imprimeavg(grouped_regions,region,type_c_o)
    plotting.imprimetot(grouped_regions,region,type_c_o)
    
    return