import os
import re

PATH = '/home/daniel/data/Documentos/recibos'

regex = re.compile('Banrisul_Recibo_(\d\d)(\d{1,2})(\d\d\d\d)_.*\.pdf')

for file in os.listdir(PATH):
    match = regex.match(file)
    if match:
        new_folder = f'{match.group(3)}-{match.group(2).rjust(2, "0")}'
        try:
            os.mkdir(os.path.join(PATH, new_folder))
        except FileExistsError:
            pass

        os.rename(os.path.join(PATH, file),
                  os.path.join(PATH, new_folder, file))
