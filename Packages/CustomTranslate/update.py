#pip install panda
#pip install ipython
#pip install file-magic
#pip install python-magic-bin
import magic
import pandas as pd
import os
import shutil

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
            print(path + file)
            ############################## Lendo arquivo
            fileN = file+'.new'
            ################ SOURCE
            filename_detected = magic.detect_from_filename(path + file)
            print(filename_detected)

            with open(path + file,"r", encoding="utf-8") as source:
                texto = source.readlines()
                print(texto)

            ################ DESTINITY
            with open(fileN,"w", encoding="utf-8") as destinity:
                for frase in texto:
                    if field in frase:
                        frase = field +"="+description
                        print("=============",frase)
                    destinity.writelines(frase)

            ################ GERAR COPIAS
            i = 1
            fileO = file + '.bk'
            path2 = 'backup/'
            if not os.path.isdir(path2):
                os.mkdir(path2)
            while os.path.isfile(path2 + fileO):
                fileO = file + str(i) + '.bk'
                i = i + 1

            shutil.copyfile(path + file, path2 + fileO)
            shutil.copyfile(fileN, path + file)

        else:
            print(" ERRO ao acessar arquivo",file)

print("Fim do processamento")