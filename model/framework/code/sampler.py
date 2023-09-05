from tqdm import tqdm
from rdkit import DataStructs
from rdkit.Chem import AllChem
from rdkit import Chem
from exmol import run_stoned
    

class StonedSingleSampler(object):
    def __init__(self, max_mutations=2, min_mutations=1, min_similarity=0.6, max_similarity=0.9):
        self.max_mutations = max_mutations
        self.min_mutations = min_mutations
        self.min_similarity = min_similarity
        self.max_similarity = max_similarity

    def _sample(self, smiles, n):
        return run_stoned(
            smiles,
            num_samples=n,
            max_mutations=self.max_mutations,
            min_mutations=self.min_mutations,
        )

    def _select_by_similarity(self, smiles_list):
        sel_smiles = []
        for smi in tqdm(smiles_list):
            mol = Chem.MolFromSmiles(smi)
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
            sim = DataStructs.TanimotoSimilarity(fp, self.seed_fps)
            print(sim)
            if sim < self.min_similarity or sim > self.max_similarity:
                continue
            sel_smiles += [smi]
        return sel_smiles

    def sample(self, smiles, n):
        self.seed_fps = AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(smiles), 2)
        sampled_smiles = []
        sampled_sim = []
        sampled = self._sample(smiles, n)
        sampled_smiles += sampled[0]
        sampled_sim += sampled[1]
        print(len(sampled_smiles), "molecules sampled. Selecting the best by similarity.")
        sampled_smiles = self._select_by_similarity(sampled_smiles)
        print("Molecules remaining", len(sampled_smiles))
        return sampled_smiles

