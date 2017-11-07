# Taxonomy

## Overview

1. Gather collection of fasta files.
2. Use "mothur" to merge them together, keeping track of different files as "groups."
3. Use "mothur" to classify sequences by comparing them to a reference genome.


## Get Sequences

Example: Use collection of 16sRNA fasta files from different Tara Ocean sample sites.


## Use Mothur to Merge and Classify

### Launch Mothur

Launching Mothur opens up a mothur interface where we can enter commands.

```bash
# Launch mother
mothur
```

The interface looks like this:

```bash
mothur v.1.38.1
Last updated: 8/9/2016

by
Patrick D. Schloss

Department of Microbiology & Immunology
University of Michigan
pschloss@umich.edu
http://www.mothur.org

When using, please cite:
Schloss, P.D., et al., Introducing mothur: Open-source, platform-independent, community-supported software for describing and comparing microbial communities. Appl Environ Microbiol, 2009. 75(23):7537-41.

Distributed under the GNU General Public License

Type 'help()' for information on the commands that are available

Type 'quit()' to exit program


mothur >
```


### Make Groups

We will merge all Fasta files from different sites together in order to compare them. First we must make groups so Mothur can identify the different files.

```bash
# Make groups
mothur > make.group(fasta=[file1.fasta]-[file2.fasta], groups=[group1]-[group2])

# For example:
mothur > make.group(fasta=ERR598944_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599001_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599078_MERGED_FASTQ_16SrRNA_10000.fasta, groups=meso-transect-surface)
```

This generates a file that ends in ".groups". For example,
```
ERR598980_MERGED_FASTQ_16SrRNA_10000.ERR598995_MERGED_FASTQ_16SrRNA_10000.ERR599142_MERGED_FASTQ_16SrRNA_10000.groups
```
If you gave it lots of input files, you might just get an output called
`mergegroups`.


Take a look with less.

(Hint: you can use the command `system()` if you want to use Unix commands while you are using mothur.)

```
mothur > system(less [groups file name])
```

### Merge Files

Now we can merge the files together. The group file will record which sequences came from which file.

```bash
# Merge files together
mothur > merge.files(input=[file1.fa]-[file2.fa]-[file3.fa], output=merged.fa)

# For example:
mothur > merge.files(input=ERR598944_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599001_MERGED_FASTQ_16SrRNA_10000.fasta-ERR599078_MERGED_FASTQ_16SrRNA_10000.fasta, output=merged.fa)
```

### Classify Sequences

Now classify sequences by comparing them to a reference database. For example, can use the SILVA database.

```bash
# classify
mothur > classify.seqs(fasta=merged.fa, group=[your groups file], reference=/usr/local/data/silva_databases/silva.seed_v119.align, taxonomy=/usr/local/data/silva_databases/silva.seed_v119.tax)

# For eaxmple:
mothur > classify.seqs(fasta=merged.fa, group=ERR598980_MERGED_FASTQ_16SrRNA_10000.ERR598995_MERGED_FASTQ_16SrRNA_10000.ERR599142_MERGED_FASTQ_16SrRNA_10000.groups, reference=/usr/local/data/silva_databases/silva.seed_v119.align, taxonomy=/usr/local/data/silva_databases/silva.seed_v119.tax)
```

> *Note:* You will see lots of warnings along the lines of: "[WARNING]: xxx could not be classified." We are going to have to leave these sequences out of the analysis! This means all of the unknowns will be grouped together even though they most likely repesent many different species, so they will be missing from our diversity analyses later on. This is why OTUs are often a better way to go here, but unfortunately our metagenomic data is too messy to be able to make nice OTUs.


## Analyze Files

Copy these files over to local computer with FileZilla or SCP.

Open the file that is called 'merged.seed_v119.wang.tax.summary' in Excel. (You may have to change the name so the file ends in '.txt' or Excel won't recognize it as a valid file to open.)

Columns:

1. `taxlevel`
Taxonomic level is in the farthest left-hand column. The lower the number, the larger the phylogenetic classification. For example, Archaea, Bacteria, Eukarya, and 'unknown' are taxonomic level 1. Taxonomic level 2 goes down a bit deeper: it classifies different phyla of Archaea, Bacteria, and Eukaryotes. Taxonomic level 3 classifies different classes of those phyla, and so on.
2. `rankID`
The rankID provides a means of keeping track of where that particular organism falls. For example, the SAR_11 clade is rankID 0.2.17.2.9, which means it is a clade within the Alphaproteobacteria (0.2.17.2), which are a clade within the Proteobacteria (rankID 0.2.17), which is a clade within the Bacteria (rankID 0.2).
3. `taxon`
The taxon column tells you the name of the taxon.
4. `daugtherlevels`
The daugther level tells you how may levels down you are in the phylogeny.
The 'total' tells you how many total sequences are within that taxonomic category.
5. Each of the following columns gives you the taxonomic breakdown for that sample.

It is useful to sort by `taxlevel.`
