import requests
import os.path
import pandas as pd
import re

df = pd.read_csv('https://raw.githubusercontent.com/EvgeniyNam/Coordination-informed-protein-descriptors/Extracting-data/ID_file.csv')

nomad_app = 'https://repository.nomad-coe.eu/app/api/'
nomad_rep = nomad_app + 'repo/'    # calc's metadata
nomad_raw = nomad_app + 'raw/'     # unprocessed calc's

upload_id = df['Upload_ID']
entry_id = df['Entry_id']

file_name = 'FHIaims.out'

df['Total_energy'] = None
counter = 0

for i in range(len(df['Upload_ID'])):
    url = nomad_rep + df['Upload_ID'][i] + '/' + df['Entry_id'][i]
    metadata = requests.get(url).json()

    calc_path = os.path.dirname(metadata['mainfile'] )
    file_name_full = calc_path + '/' + file_name

    url = nomad_raw + df['Upload_ID'][i] + '/' + file_name_full
    response = requests.get(url)

    content = response.content.decode('utf-8')  # декодируем содержимое файла

    pattern = r'Total energy of the DFT / Hartree-Fock s\.c\.f\. calculation\s*:\s*(-?\d+\.\d+)'
    matches = re.findall(pattern, content)
    df.at[i, 'Total_energy'] = matches[0]
    print(counter)
    print(df['Total_energy'][i])
    counter += 1
else:
    print('Сделано!')

df.to_csv('Total_energy_raw.csv', index=False)