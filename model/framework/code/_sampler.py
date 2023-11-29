from tqdm import tqdm
from rdkit import DataStructs
from rdkit.Chem import AllChem
from rdkit import Chem
from exmol import run_stoned


def calculate_similarity(ref_mol, mol_list):
    ref_fp = AllChem.GetMorganFingerprint(ref_mol, 2)
    mol_fps = [AllChem.GetMorganFingerprint(mol, 2) for mol in mol_list]
    similarities = [
        DataStructs.TanimotoSimilarity(ref_fp, mol_fp) for mol_fp in mol_fps
    ]
    return similarities

def sort_molecules_by_similarity(ref_mol, mol_list):
    similarities = calculate_similarity(ref_mol, mol_list)
    paired = list(zip(mol_list, similarities))
    sorted_mols = sorted(paired, key=lambda x: x[1], reverse=True)
    print("Sorted mols", len(sorted_mols))
    return [mol for mol, _ in sorted_mols]

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
            if sim < self.min_similarity or sim > self.max_similarity:
                continue
            sel_smiles += [smi]
        print(len(smiles_list), "original sampled smiles")
        print(len(sel_smiles), "selected smiles")
        return sel_smiles
    
    def _sort_smiles(self, origin_smiles, sampled_smiles):
        ref_mol = Chem.MolFromSmiles(origin_smiles)
        if len(sampled_smiles) == 0:
            return []
        mol_list = []
        for smi in sampled_smiles:
            mol = Chem.MolFromSmiles(smi)
            if mol is None:
                continue
            mol_list += [mol]
        sorted_mols = sort_molecules_by_similarity(ref_mol, mol_list)
        sorted_smiles = []
        for m in sorted_mols:
            if m is None:
                continue
            sorted_smiles += [Chem.MolToSmiles(m)]
        return sorted_smiles

    def sample(self, smiles, n):
        self.seed_fps = AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(smiles), 2)
        sampled_smiles = []
        sampled = self._sample(smiles, n)
        sampled_smiles += sampled[0]
        print(len(sampled_smiles), "molecules sampled. Selecting the best by similarity.")
        sampled_smiles = self._select_by_similarity(sampled_smiles)
        print("Molecules remaining", len(sampled_smiles))
        sampled_smiles_ordered = self._sort_smiles(smiles, sampled_smiles)
        sampled_smiles_selected = sampled_smiles_ordered[:100]
        return sampled_smiles_selected
    
