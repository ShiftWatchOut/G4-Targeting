from rdkit import Chem
from rdkit.Chem import Draw
from rdkit import DataStructs

if __name__ == '__main__':
    smi = 'C[C@@H]([C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CC[C@@H]4[C@@]3(CC[C@@H](C4)[N+](C)(C)C)C)C)[N+](C)(C)C.[Cl-].[Cl-]'
    m = Chem.MolFromSmiles(smi)
    Draw.MolToImageFile(m, 'mol.jpg', (800, 800))