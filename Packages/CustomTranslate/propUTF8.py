#pip install panda
#pip install ipython
#pip install file-magic
#pip install python-magic-bin
import magic
import os
from os import chdir, getcwd, listdir
from os.path import isfile
import re

cwd = os.getcwd()

path = '/var/www/dataverse/langBundles/'
chdir(path)

cmd = ""

for c in listdir():
    if os.path.isfile(path + c):
        if ('.prop' in c):
            fd = str(magic.detect_from_filename(path + c))
            idp1 = fd.find('encoding=') + 10
            idp2 = fd.find(', name=') -1
            decod = fd[idp1:idp2]

            if (decod == 'iso-8859-1'):
                print("=>"+path + c)
                print(decod,c)
                print("=========================")
                cmd = cmd + 'iconv -f ISO-8859-1 -t UTF-8 ' + path+c + ' > ' + path+c + chr(13)

if (len(cmd) > 0):
    chdir(cwd)
    with open('convert',"w", encoding="utf-8") as destinity:
        destinity.writelines(cmd)

print("Fim do processamento")