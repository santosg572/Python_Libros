#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cc = """
Created on Fri Jan  7 05:05:36 2022

@author: santosg \n

Este programa saca la lista de directorios que se encuentran
 
dentro de un directorio padre, en este caso es './'

"""

import sys
import time
import funcionesLinux

print(cc)
time.sleep(3)

val = input("Mete el directorio padre [./]: ")

dir1 = './'

if len(val) > 0:
    dir1 = val


res = funcionesLinux.SacaLista_Dir_Otro(dir1)

if len(res) > 0:
    print(res)
else:
    print('NO HUBO Directorios')