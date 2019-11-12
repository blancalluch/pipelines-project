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
import datos

def recibeConfig():
    parser = argparse.ArgumentParser(description='Consumo de aguacate')
    parser.add_argument('--Year',
                        help='Año que quieres observar (2015/2016/2017/2018)',
                        default="2015"
                        )
    parser.add_argument('--Region',
                        help='Region donde ha sido la venta de aguacates.',
                        default="Atlanta"
                        )
    parser.add_argument('--Type',
                        help='Tipo de aguacate (conventional/organic)',
                        default="organic"
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
    year=config.Year
    region=config.Region
    type_c_o=config.Type
    print("Year {}".format(year))
    print("Region {}".format(region))
    print("Type {}".format(type_c_o))
    info_list=datos.getDatos(year,region,type_c_o)
    #print(info_list)
    print("Avg price of the year:{}".format(info_list[0]))
    print("Total Volume sold per week that year:{}".format(info_list[1]))
    print("Address of a supermarket in {}:{}".format(region,info_list[2]))
    print("Name of supermarket:{}".format(info_list[3]))
    


if __name__=="__main__":
    main()