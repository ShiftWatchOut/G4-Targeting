from rdkit import Chem
from rdkit.Chem.Draw import SimilarityMaps
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mol = Chem.MolFromSmiles('COc1cccc2cc(C(=O)NCCCCN3CCN(c4cccc5nccnc54)CC3)oc21')
    refmol = Chem.MolFromSmiles('CCCN(CCCCN1CCN(c2ccccc2OC)CC1)Cc1ccc2ccccc2c1')
    fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, mol, SimilarityMaps.GetMorganFingerprint)
    handlelim = [0, 1]
    # plt.xlim(handlelim)
    # plt.ylim(handlelim)
    # plt.show()