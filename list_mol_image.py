import os
import re
from rdkit import Chem
from rdkit.Chem import Draw
import pandas as pd


# 创建按 target 分类的子文件夹
def makeFolder():
    file_list = os.listdir()
    new_list = [re.sub(r'.xlsx', '', s) for s in file_list]
    i = 0
    j = 0
    for x in new_list:
        if os.path.exists(x):
            j += 1
            continue
        else:
            os.mkdir(x)
            i += 1
    print('总创建了', i, '个文件夹，有', j, '个文件夹已经存在无法重复创建')
    # return new_list


def get_image(target):      # target 即是目标文件夹名
    df = pd.read_excel(target + '.xlsx')
    last_idx = ''
    for smile, idx in zip(df['Smiles'], df['Ligand ID']):
        if idx == last_idx:
            continue
        else:
            if idx == 'G4L1075':
                continue
            os.chdir(target)    # 跳转至目标文件夹
            m = Chem.MolFromSmiles(smile)
            Draw.MolToFile(m, idx+'.png',(900, 900))
            last_idx = idx
            os.chdir('..')      # 最后创建好了返回上级文件夹


if __name__ == '__main__':
    os.chdir('classify')    # 转入分类文件夹
    i = 0
    makeFolder()
    target_list = ['AGAGGGAGGGCGCTGGGAGGAGGGGCT', 'AGGGAGGGCGCTGGGAGGAGGG', 'AGGGCGGTGTGGGAAGAGGGAAGAGGGGGAGG',
               'AGGGGCGGGCGCGGGAGGAAGGGGGCGGGAGCGGGGCTG', 'AGGGTGGGGAGGGTGGG', 'AGGGTGGGGAGGGTGGGG',
               'AGGGTTAGGGTTAGGGTTAGGG', 'AGGGTTAGGGTTAGGGTTAGGGT', 'CCCGGGCGGGCGCGAGGGAGGGGAGG',
               'CGGGCGCGGGAGGAAGGGGGCGGGAGC', 'CGGGCGGGCGCGAGGGAGGGG', 'F21T G4', 'GGCATAGTGCGTGGGCGTTAGC',
               'GGGAGGGCGCTGGGAGGAGGG', 'GGGCGCGGGAGGAATTGGGCGGG', 'GGGCGGGCGCGAGGGAGGGG', 'GGGTGGGTAGGGTGGG',
               'GGGTGTGGGTGTGGGTGTGGG', 'GGGTTAGGGTTAGGGTTAGGG', 'GTTAGGGTTAGGGTTAGGGTTAGGGTTAGG',
               'TATAGCTATA-HEG-TATAGCTATA', 'TATAGCTATA', 'TATAGCTATATTTTTTTATAGCTATA', 'TGAGGGTGGGTAGGGTGGGTAA',
               'TGGGGAGGGTGGGGAGG', 'TGGGGAGGGTGGGGAGGGTGGGGAAGG', 'TTAGGC', 'TTAGGG']
    for x in target_list:
        i += 1
        print(i, x)
        get_image(x)
