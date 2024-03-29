import os # bliblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos

import pandas as pd

from typing import List

"""
função para ler os arquivos de uma pasta/input e retornar uma lista de dataframes

args: input_path(str): caminho da pasta com os arquivos
return: list: lista de dataframe
"""

path = 'C:/Users/kevyn/Projetos/jornada/workshop/estrutura_workshop/data/input/'

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path,"*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)