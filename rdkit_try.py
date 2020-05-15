from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import SimilarityMaps
import matplotlib.pyplot as plt

if __name__ == '__main__':
    targetmol = Chem.MolFromSmiles('O=C(CNNC1CCCC1)Nc2cccc(c2)c3cn(nn3)c4ccc5cc6ccc(cc6nc5c4)n7cc(nn7)c8cccc(NC(=O)CNNC9CCCC9)c8')
    refmol = Chem.MolFromSmiles('O=C(CNN1CCCCC1)Nc2cccc(c2)c3cn(nn3)c4ccc5cc6ccc(cc6nc5c4)n7cc(nn7)c8cccc(NC(=O)CNN9CCCCC9)c8')
    target_mol_simi_fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, targetmol,
                                                                                   SimilarityMaps.GetMorganFingerprint)
    plt.show()
