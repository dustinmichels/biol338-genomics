See Week 4 on [Protocals.io](https://www.protocols.io/view/week-4-calling-open-reading-frames-with-prodigal-u-js3cngn?step=4)

## Finishing up from last week

Get to folder from last week, with reads
```shell
ssh [username]@baross.its.carleton.edu
cd project_directory/
cd out/
```

Change name of contig-100.fa to conventional name for class,
Run script so that another software program (called “anvi’o") is happy,
Copy formatted, assembled file to shared class directory.
```shell
mv contig-100.fa ERR599031_assembly.fasta
anvi-script-reformat-fasta ERR599031_assembly.fasta -o ERR599031_assembly_formatted.fasta -l 0 --simplify-names
cp ERR599031_assembly_formatted.fasta /usr/local/data/class_shared
```

## Looking for open reading frames

Back to toy dataset 
```shell
cp /usr/local/data/toy_datasets/toy_dataset_assembly_subsample.fa toy_assembly
mkdir ORF_finding
cd ORF_finding
```

Run prodigal
```
prodigal -i ../toy_assembly/toy_dataset_assembly_subsample.fa -o toy_assembly_ORFs.gbk -a toy_assembly_ORFs.faa -p single
```

Note:
* The “-i” flag gives the input file, which is the assembly you just made.
* The “-o” flag gives the output file in Genbank format
* The ‘-a” flag gives the output file in fasta format
* The “-p” flag states which procedure you’re using: whether this is a single genome or a metagenome. This toy dataset is a single genome so we are using –p single, but for your project dataset, you will use –p meta.

See amino acids:
```
less toy_assembly_ORFs.faa
```

Do a protein blast on https://blast.ncbi.nlm.nih.gov/Blast.cgi
* Try protein blastp, and tblastn

*What's the difference?*
> blastp is a protein-protein blast. When you run it online like this, you are comparing your protein sequence against the National Centers for Biotechnology Information (NCBI) non-redundant protein database, which is a giant database of protein sequences that is “non-redundant”—that is, each protein should be represented only once. In contrast, tblastn is a translated nucleotide blast. You are blasting your protein sequence against a translated nucleotide database. When you run it online like this, you are comparing your protein sequence against the NCBI non-redundant nucleotide database, which is a giant database of nucleotide sequnces, which can include whole genomes.

Get rid of asterisks using sed
```
sed 's/\*//g' toy_assembly_ORFs.faa > toy_assembly_ORFs.noasterisks.faa
```

Run interproscan
```
interproscan.sh -i toy_assembly_ORFs.noasterisks.faa -f tsv
```





