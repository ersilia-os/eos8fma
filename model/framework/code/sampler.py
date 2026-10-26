import random

from rdkit import DataStructs
from rdkit.Chem import AllChem
from rdkit import Chem
from exmol import run_stoned

N_OUTPUTS = 100


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
        """Candidates inside the similarity window as (canonical SMILES, similarity) pairs, one per molecule."""
        selected = {}
        for smi in smiles_list:
            mol = Chem.MolFromSmiles(smi)
            if mol is None:
                continue
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
            sim = DataStructs.TanimotoSimilarity(fp, self.seed_fps)
            if sim < self.min_similarity or sim > self.max_similarity:
                continue
            selected[Chem.MolToSmiles(mol)] = sim
        return list(selected.items())

    def sample(self, smiles, n):
        ref_mol = Chem.MolFromSmiles(smiles)
        if ref_mol is None:
            raise ValueError("RDKit cannot parse the input SMILES")
        self.seed_fps = AllChem.GetMorganFingerprintAsBitVect(ref_mol, 2)
        sampled_smiles = self._sample(smiles, n)[0]
        candidates = self._select_by_similarity(sampled_smiles)
        # Pick at random inside the window: keeping the most similar candidates would make
        # the similarity of the output a property of the selection, not of the generator.
        picked = random.sample(candidates, min(N_OUTPUTS, len(candidates)))
        # Listed most similar first (same bit-vector similarity as the window)
        picked.sort(key=lambda pair: pair[1], reverse=True)
        selected = [smi for smi, _ in picked]
        if len(selected) < N_OUTPUTS:
            selected.extend([None] * (N_OUTPUTS - len(selected)))
        return selected
