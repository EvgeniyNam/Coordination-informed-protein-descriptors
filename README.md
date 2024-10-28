# Coordination-Informed Protein Embedings

This repository introduces a novel approach that employs property-based protein embeddings,
with a particular focus on the role of double-charged cations such as Ca<sup>2+</sup> and Mg<sup>2+</sup>.

In this framework, each amino acid is assigned not only standard cheminformatics descriptors
but also the interaction energies Mg<sup>2+</sup>, Ca<sup>2+</sup>, and Ba<sup>2+</sup>,
aiming to enhance machine learning applications in protein characterization.

In this repository, we provide the interaction energy values for ions with amino acids that were utilized in our research.
We believe these data will be valuable for researchers in cheminformatics and related fields,
facilitating further exploration and application in protein studies.


## Dataset

This dataset comprises a table where each row corresponds to an amino acid,
and the columns represent the interaction energies between
the amino acids and double-charged cations in the gas phase (see Figure 1).

<img src="images/figure_1.png" width="80%">

*Figure 1. Reaction corresponding to the provided interaction energies*

For amino acids with potentially ionic side chains, only charged forms were considered:
cationic forms for Lysine (Lys), Arginine (Arg), and Histidine (His);
and anionic forms for Aspartic acid (Asp) and Glutamic acid (Glu). 
This approach was adopted to enhance the diversity of the final vectors,
thereby improving their effectiveness as machine learning descriptors.

**Table 1. AA-M<sup>2+</sup> Interaction energies, kJ/mol.**


## [Data processing](data_processing/)

The original data on interaction energies between amino acids and double-charged ions were published in [Nature Scientific Data](https://www.nature.com/articles/sdata20169).
The raw data was sourced from the [NOMAD database](https://nomad-lab.eu/prod/v1/gui/search/entries?datasets.dataset_name=Cation-coordinated%20conformers%20of%2020%20proteinogenic%20amino%20acids%20with%20different%20protonation%20states).

The dataset models amino acids with the following modifications (**Figure 2**):
- The carboxylic acid (-COOH) group is transformed to an amide (-CONHMe).
- The α-amino group (-NH2) is acylated to form an amide (-NHCOMe).
- Both neutral and charged states are considered for potentially ionic side chains:
    - cationic forms for Lysine (Lys), Arginine (Arg), and Histidine (His);
    - anionic forms for Aspartic acid (Asp) and Glutamic acid (Glu).
- All computations were performed in the gas phase.

<img src="images/figure_2.png" width="100%">

*Figure 2. Modified aminoacids structures*

The dataset includes all identified conformers for these 20 amino acids in both free and bound states (complexes with Mg, Ca, Ba).
For this repository, we have used the lowest energy conformer for each system.

For detailed information on the data extraction process, please refer to the [data_processing](data_processing/).

