from rdkit import Chem
from rdkit.Chem import Draw
smi = 'C[n+]1ccc(cc1)c2c3C=Cc(n3)c(c4cc[n+](C)cc4)c5ccc([nH]5)c(c6cc[n+](C)cc6)c7ccc(n7)c(c8C=Cc2[nH]8)c9cc[n+](C)cc9'
m = Chem.MolFromSmiles(smi)
Draw.MolToImageFile(m, "mol.jpg")