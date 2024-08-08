# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

TAB = b'\t'
PUNTOYCOMA= b';'
file_path2 = r"c:/Users/josen/Downloads/202309 kk.txt"

# relative or absolute file path, e.g.:
file_path = r"c:/Users/josen/Downloads/202309 L.A.R. KAPURA - LAR DT CSV(1).tsv"
file_path_salida = r"c:/Users/josen/Downloads/202309 kk.txt"

file_path2= r"D:/Downloads/202310 L.A.R. KAPURA - LAR DT CSV (4).tsv"
file_path_salida2 = r"d:/Downloads/202310 L.A.R. KAPURA.csv"


with open(file_path2, 'rb') as open_file:
#with open(file_path, 'rb',encoding='cp1252') as open_file:
    content = open_file.read()
    
# Windows ➡ Unix
content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

# Unix ➡ Windows
# content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

# reemplazar tab por ;
content = content.replace(TAB, PUNTOYCOMA)

with open(file_path_salida2, 'wb') as open_file:
    open_file.write(content)


# necesito que el archivo de salida salga en unix ANSI y esta saliendo en unix UTF8...


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:43:19 2023

@author: josen
"""
