#!/usr/local/bin/python3

import sys
import argparse
import subprocess
import pandas as pd 
import getpass
import json
import os
import requests
import re
import getDatos

def recibeConfig():
    parser = argparse.ArgumentParser(description='Consumo de aguacate')
    parser.add_argument('--Date',
                        help='Semana que quieres observar: YYYY-MM-DD',
                        default="2015-01-04"
                        )
    parser.add_argument('--Region',
                        help='Region donde ha sido la venta de aguacates.',
                        default="Atlanta"
                        )

    args = parser.parse_args()
    print(args)
    return args

def main():
    # Pipeline

    print(sys.argv)
    
    # PASO 1 - Recibir flags y estandarizarlos en un dict
    config = recibeConfig()
    
    # PASO 2 - imprimir datos
    fecha=config.Date
    region=config.Region
    print("Week {}".format(fecha))
    print("Region {}".format(region))
    
    info_list=getDatos(fecha,region)
    print(info_list)
    print("Avg price of that week:{}".format(info_list[0]))
    print("Total Volume sold that week:{}".format(info_list[1]))
    #df = getDatos(config.url)
    #df_clean = cleanDf(df)

if __name__=="__main__":
    main()