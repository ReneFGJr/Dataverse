#pip install panda
#pip install ipython
#pip install file-magic
#pip install python-magic-bin
import magic
import os
from os import chdir, getcwd, listdir
from os.path import isfile
import re

path = '/var/www/dataverse/langBundles/'
chdir(path)

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

print("Fim do processamento")