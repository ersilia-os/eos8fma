# Stoned Sampler

The STONED sampler uses small modifications to molecules represented as SELFIES to perform a search of the chemical space and generate new molecules. The use of string modifications in the SELFIES molecular representation bypasses the need for large amounts of data while maintaining a performance comparable to deep generative models.

This model was incorporated on 2023-08-08.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8fma`
- **Slug:** `stoned-sampler`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Generation`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1000`
- **Output Consistency:** `Variable`
- **Interpretation:** Up to 1000 derivatives of the input molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smiles_000 | string |  | Generated molecule index 0 using the STONED molecular generator |
| smiles_001 | string |  | Generated molecule index 1 using the STONED molecular generator |
| smiles_002 | string |  | Generated molecule index 2 using the STONED molecular generator |
| smiles_003 | string |  | Generated molecule index 3 using the STONED molecular generator |
| smiles_004 | string |  | Generated molecule index 4 using the STONED molecular generator |
| smiles_005 | string |  | Generated molecule index 5 using the STONED molecular generator |
| smiles_006 | string |  | Generated molecule index 6 using the STONED molecular generator |
| smiles_007 | string |  | Generated molecule index 7 using the STONED molecular generator |
| smiles_008 | string |  | Generated molecule index 8 using the STONED molecular generator |
| smiles_009 | string |  | Generated molecule index 9 using the STONED molecular generator |

_10 of 1000 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8fma](https://hub.docker.com/r/ersiliaos/eos8fma)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8fma.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8fma.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `867`
- **Image Size (Mb):** `772.07`

**Computational Performance (seconds):**
- 10 inputs: `77.48`
- 100 inputs: `-1`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/aspuru-guzik-group/stoned-selfies](https://github.com/aspuru-guzik-group/stoned-selfies)
- **Publication**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8153210/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8153210/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8fma
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8fma
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
