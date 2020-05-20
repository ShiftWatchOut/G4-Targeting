import pandas as pd
import file_sheet_name as fsname

target_list = ['AGAGGGAGGGCGCTGGGAGGAGGGGCT', 'AGGGAGGGCGCTGGGAGGAGGG', 'AGGGCGGTGTGGGAAGAGGGAAGAGGGGGAGG',
               'AGGGGCGGGCGCGGGAGGAAGGGGGCGGGAGCGGGGCTG', 'AGGGTGGGGAGGGTGGG', 'AGGGTGGGGAGGGTGGGG',
               'AGGGTTAGGGTTAGGGTTAGGG', 'AGGGTTAGGGTTAGGGTTAGGGT', 'CCCGGGCGGGCGCGAGGGAGGGGAGG',
               'CGGGCGCGGGAGGAAGGGGGCGGGAGC', 'CGGGCGGGCGCGAGGGAGGGG', 'F21T G4', 'GGCATAGTGCGTGGGCGTTAGC',
               'GGGAGGGCGCTGGGAGGAGGG', 'GGGCGCGGGAGGAATTGGGCGGG', 'GGGCGGGCGCGAGGGAGGGG', 'GGGTGGGTAGGGTGGG',
               'GGGTGTGGGTGTGGGTGTGGG', 'GGGTTAGGGTTAGGGTTAGGG', 'GTTAGGGTTAGGGTTAGGGTTAGGGTTAGG',
               'TATAGCTATA-HEG-TATAGCTATA', 'TATAGCTATA', 'TATAGCTATATTTTTTTATAGCTATA', 'TGAGGGTGGGTAGGGTGGGTAA',
               'TGGGGAGGGTGGGGAGG', 'TGGGGAGGGTGGGGAGGGTGGGGAAGG', 'TTAGGC', 'TTAGGG']

tar_num = {'AGAGGGAGGGCGCTGGGAGGAGGGGCT': 0, 'AGGGAGGGCGCTGGGAGGAGGG': 1, 'AGGGCGGTGTGGGAAGAGGGAAGAGGGGGAGG': 2, 'AGGGGCGGGCGCGGGAGGAAGGGGGCGGGAGCGGGGCTG': 3, 'AGGGTGGGGAGGGTGGG': 4, 'AGGGTGGGGAGGGTGGGG': 5, 'AGGGTTAGGGTTAGGGTTAGGG': 6, 'AGGGTTAGGGTTAGGGTTAGGGT': 7, 'CCCGGGCGGGCGCGAGGGAGGGGAGG': 8, 'CGGGCGCGGGAGGAAGGGGGCGGGAGC': 9, 'CGGGCGGGCGCGAGGGAGGGG': 10, 'F21T G4': 11, 'GGCATAGTGCGTGGGCGTTAGC': 12, 'GGGAGGGCGCTGGGAGGAGGG': 13, 'GGGCGCGGGAGGAATTGGGCGGG': 14, 'GGGCGGGCGCGAGGGAGGGG': 15, 'GGGTGGGTAGGGTGGG': 16, 'GGGTGTGGGTGTGGGTGTGGG': 17, 'GGGTTAGGGTTAGGGTTAGGG': 18, 'GTTAGGGTTAGGGTTAGGGTTAGGGTTAGG': 19, 'TATAGCTATA-HEG-TATAGCTATA': 20, 'TATAGCTATA': 21, 'TATAGCTATATTTTTTTATAGCTATA': 22, 'TGAGGGTGGGTAGGGTGGGTAA': 23, 'TGGGGAGGGTGGGGAGG': 24, 'TGGGGAGGGTGGGGAGGGTGGGGAAGG': 25, 'TTAGGC': 26, 'TTAGGG': 27}


def target2num():
    df = pd.read_excel(fsname.inputFile, fsname.sheetName1)
    # df.replace(target_list, range(0, 28))
    tmp_df = df.drop(
        columns=['Value type', 'Value1', 'Value2', 'Target ID', 'activity', 'Formula', 'Ligand name'])
    # tmp_df.replace(target_list, range(0, 28), inplace=True)
    tmp_df.replace(tar_num, inplace=True)
    tmp_df.dropna().to_excel('clean_data.xlsx', index=False)


def generate_dict():
    d = {}
    for i in range(0, 28):
        d[target_list[i]] = i
    print(d)


if __name__ == '__main__':
    generate_dict()
