# Stoned Sampler

The STONED sampler uses small modifications to molecules represented as SELFIES to perform a search of the chemical space and generate new molecules. The use of string modifications in the SELFIES molecular representation bypasses the need for large amounts of data while maintaining a performance comparable to deep generative models.

## Identifiers

* EOS model ID: `eos8fma`
* Slug: `stoned-sampler`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: Up to 1000 derivatives of the input molecule

## References

* [Publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8153210/)
* [Source Code](https://github.com/aspuru-guzik-group/stoned-selfies)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos8fma)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8fma.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos8fma) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8153210/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!