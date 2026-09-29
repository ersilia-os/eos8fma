# imports
import os
import csv
import sys
from sampler import StonedSingleSampler, N_OUTPUTS

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# raw STONED candidates drawn per input; only those inside the similarity window are kept
N_RAW_SAMPLES = 5000

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
sampler = StonedSingleSampler()
outputs = []
for smi in smiles_list:
    try:
        o = sampler.sample(smi, N_RAW_SAMPLES)  # "sample" keeps the N_OUTPUTS most similar candidates
    except Exception:
        o = [""] * N_OUTPUTS
    outputs += [o]

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["smi_{0}".format(str(i).zfill(2)) for i in range(N_OUTPUTS)])  # header
    for o in outputs:
        writer.writerow(o)
