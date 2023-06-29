#pip install panda
#pip install ipython

import csv
import pandas as pd
from IPython.display import display
import os
import math
import numpy as np

translates = pd.read_csv("customTranslate.csv",sep=";")
linhas = len(translates)
path = '/var/www/dataverse/langBundles/'

for ln in range(linhas):
    if (ln >= 10):
        print("Header")
    else:
        file = translates.iloc[ln]['file']
        lang = translates.iloc[ln]['lang']
        field = translates.iloc[ln]['field']
        description = translates.iloc[ln]['translate']
        lang = str(lang)
        ################# Seleciona arquivo de idioma
        if (lang != 'nan'):
            file += '_'+lang

        file += '.properties'

        ####################### Arquivo
        if os.path.isfile(path + file):
            print("================== P R O C E S S A N D O ==")
            print(file)
            ############################## Lendo arquivo
            fileN = file+'.new'
            ################ SOURCE
            with open(path + file,"r", encoding="utf-8") as source:
                texto = source.readlines()

            ################ DESTINITY
            with open(fileN,"w", encoding="utf-8") as destinity:
                for frase in texto:
                    if field in frase:
                        frase = field +"="+description
                        print("=============",frase)
                    destinity.writelines(frase)

            ################ GERAR COPIAS
            i = 1
            fileO = file+'.bk'
            while os.path.isfile(fileO):
                fileO = file + i + '.bk'
                i = i + 1
            print("========"+fileO)

        else:
            print(" ERRO ao acessar arquivo",file)

print("O DataFrame contém {0} linhas".format(linhas))
