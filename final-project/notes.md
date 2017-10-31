# Notes

Data
https://www.ebi.ac.uk/metagenomics/projects/ERP001736/samples/ERS488769/runs/ERR599031/results/versions/2.0

- Could download functional analysis (Go annotation?)


## Copy relevant 16s

Inside `/usr/local/data/Tara_datasets`

```bash
cp */ERR599104*16SrRNA* */ERR599090*16SrRNA* */ERR598999*16SrRNA* */ERR599078*16SrRNA* */ERR598948*16SrRNA* */ERR598992*16SrRNA* ~/project_directory/taxonomy
```


## Analyze sequences with mothur


Launch: `mothur`

```mothur
make.group(fasta=ERR599104_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599090_MERGED_FASTQ_16SrRNA_10000.fasta-ERR598999_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599078_MERGED_FASTQ_16SrRNA_10000.fasta-ERR598948_MERGED_FASTQ_16SrRNA_10000.fasta-ERR598992_MERGED_FASTQ_16SrRNA_10000.fasta, groups=01_dcm_SernOcean-02_surface_SernOcean-03_meso_SPacific-04_surface_NAtlantic-05_dcm_SPacific-06_surface_SPacific)
```


Look at file in Mothur
```mothur
# look at file
system(ls)
system(less mergegroups)
```

Merge it all together
```mothur
merge.files(input=ERR599104_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599090_MERGED_FASTQ_16SrRNA_10000.fasta-ERR598999_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599078_MERGED_FASTQ_16SrRNA_10000.fasta-ERR598948_MERGED_FASTQ_16SrRNA_10000.fasta-ERR598992_MERGED_FASTQ_16SrRNA_10000.fasta, output=merged.fa)
```

Classify sequences by comparing them to a reference database (SILVA)
```mothur
classify.seqs(fasta=merged.fa, group=mergegroups, reference=/usr/local/data/silva_databases/silva.seed_v119.align, taxonomy=/usr/local/data/silva_databases/silva.seed_v119.tax, processors=20)
```

Copy files over with Filezilla / SCP
Open `merged.seed_v119.wang.tax.summary` in Excel.

Columns (quoting from handout):

* Taxonomic level is in the farthest left-hand column. The lower the number, the larger the phylogenetic classification. For example, Archaea, Bacteria, Eukarya, and 'unknown' are taxonomic level 1. Taxonomic level 2 goes down a bit deeper: it classifies different phyla of Archaea, Bacteria, and Eukaryotes. Taxonomic level 3 classifies different classes of those phyla, and so on.
* The rankID provides a means of keeping track of where that particular organism falls. For example, the SAR_11 clade is rankID 0.2.17.2.9, which means it is a clade within the Alphaproteobacteria (0.2.17.2), which are a clade within the Proteobacteria (rankID 0.2.17), which is a clade within the Bacteria (rankID 0.2).
* The taxon column tells you the name of the taxon.
* The daugther level tells you how may levels down you are in the phylogeny.
* The 'total' tells you how many total sequences are within that taxonomic category.
* Each of the following columns gives you the taxonomic breakdown for that sample.






