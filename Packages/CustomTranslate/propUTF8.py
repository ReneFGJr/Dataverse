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
            print("=>"+path + c)
            filename_detected = magic.detect_from_filename(path + c)
            print(filename_detected)

print("Fim do processamento")