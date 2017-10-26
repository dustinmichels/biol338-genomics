# Week 6

Original procedure by Rika Anderson on [protocols.io](https://www.protocols.io/private/5f2426912e927a47e8a87a7d9e23156a)

## 1. Mapping with a toy dataset



### 1.a) Make mapping dir and copy files

```bash
mkdir mapping
cd mapping

cp /usr/local/data/toy_datasets/toy_dataset_reads_for_mapping.fasta .
cp /usr/local/data/toy_datasets/toy_dataset_contig_for_mapping.fasta .
```



### 1.b) Prepare an index of reference with bowtie2

```bash
bowtie2-build toy_dataset_contig_for_mapping.fasta toy_dataset_contig_for_mapping.btindex
```
>* bowtie2-build is the program that indexes your reference.
>* The first argument gives the reference dataset name.
>* The second argument provides the name you want to give to the index.



### 1.c) Map, create SAM file with bowtie2

```bash
bowtie2 -x toy_dataset_contig_for_mapping.btindex -f -U toy_dataset_reads_for_mapping.fasta -S toy_dataset_mapped_species1.sam
```

> * Bowtie2 is the name of the mapping program.
> * `-x` is the flag that provides the name of the index you just made.
> * `-f` means that the reads you are mapping are in fasta, not fastq, format.
> * `-U` means that the reads are not paired.
> * `-S` provides the name of your output file, which is in SAM format.



### 1.d) Convert SAM file to BAM file, using samtools

```bash
samtools view -bS toy_dataset_mapped_species1.sam > toy_dataset_mapped_species1.bam
```



### 1.e) Sort BAM file

```bash
samtools sort toy_dataset_mapped_species1.bam -o toy_dataset_mapped_species1_sorted.bam
```



### 1.f) To visualize mapping, index reference again with samtools

```bash
samtools faidx toy_dataset_contig_for_mapping.fasta
samtools index toy_dataset_mapped_species1_sorted.bam
```

Using samtools faidx:

> * Samtools faidx is the name of the program that indexes the reference.
> * The first argument provides the name of the index, which should be your reference file.

Using samtools index:

> * samtools index is the name of the program that indexes the bam files.
> * The first argument provides the name of a sorted bam file.



### 1.g) Copy files to local, view with IGV viewer

Copy fies over

```bash
scp -r [your username]@liverpool.its.carleton.edu:/Accounts/[your username]/toy_dataset_directory/mapping/ ~/Desktop
```

Using IGV:

* Click  **'Genomes' --> 'Load Genome from File'**
  - select 'toy_dataset_contig_for_mapping.fasta'
* Click **'File' --> 'Load from File'**
  - Select 'toy_dataset_mapped_species1_sorted.bam'

See: http://software.broadinstitute.org/software/igv/AlignmentData



### 1.h) Compare this mapping with another one

Back on server side...

RFs.faa  ERR599031_O
```bash
# copy files
cp /usr/local/data/toy_datasets/toy_dataset_reads_for_mapping_species2.fasta .

# Alreday made index of reference

# Create SAM file (using index of reference and species2 fasta file)
bowtie2 -x toy_dataset_contig_for_mapping.btindex -f -U toy_dataset_reads_for_mapping_species2.fasta -S toy_dataset_mapped_species2.sam

# Convert SAM file to BAM file
samtools view -bS toy_dataset_mapped_species2.sam > toy_dataset_mapped_species2.bam

# Sort SAM file
samtools sort toy_dataset_mapped_species2.bam -o toy_dataset_mapped_species2_sorted.bam

# Index BAM file again for visualization
samtools index toy_dataset_mapped_species2_sorted.bam
```



## 2. Mapping project dataset



### 2.a) Run commands to map and index

```bash
# Make index of reference (assembly of contigs)
bowtie2-build ERR599031_assembly_formatted.fasta ERR599031_assembly_formatted.btindex

# Create SAM file, comparing reads to contig
bowtie2 -x ERR599031_assembly_formatted.btindex -f -U ../ERR599031_sample.fasta -S ERR599031_mapped.sam -p 4

# Convert SAM to BAM 
samtools view -bS ERR599031_mapped.sam > ERR599031_mapped.bam

# Sort BAM file
samtools sort ERR599031_mapped.bam -o ERR599031_mapped_sorted.bam

# Index reference and reads once again for visualization
samtools faidx ERR599031_assembly_formatted.fasta 
samtools index ERR599031_mapped_sorted.bam
```

We are comparing reads to the contigs made from those reads. This can tell us something about aundance of certain species and certain genes.



### 2.b) View in IGV

Note that you have many contigs as reference, rather than one scaffold, so you must toggle between them with drop-down menu.



### 2.c) Make bed file

Rather than visualize, want to quantify the average coverage of every single open reading frame.

```bash
# Make bed file from ORF file
make_bed_file_from_ORF_file.py ERR599031_ORFs.noasterisks.faa

# copy and rename bed file
cp ERR599031_ORFs.noasterisks.bed ERR599031_assembled_ORFs.bed

# move out of ORF folder, into mapping folder
mv ERR599031_assembled_ORFs.bed ../mapping
```

Use bed file to calculate read depth for every single ORF in ORF file

```bash
samtools bedcov ERR599031_assembled_ORFs.bed ERR599031_mapped_sorted.bam  > ERR599031_ORF_coverage.txt
```

### 2.d) Examine File

- Open this file in Excel, calculate average coverage
- Reference interproscan & find two ORFs of interest. See how coverage compares.
- Also: copy files to class data



### 2.e) Compare to other students

I'm at depth of 600m. Comparing to others in mesopelagic zone.

- Alief — 600m, South Pacific (near the Marquesas), ERR598999
- Adriana — 790m, Southern Ocean (near Antarctica), ERR599008

```bash
# Copy files
INCOMPLETE!!

# Make index of reference (assembly of contigs)
bowtie2-build ERR599031_assembly_formatted.fasta ERR599031_assembly_formatted.btindex

# Create SAM file, comparing reads to contig
bowtie2 -x ERR599031_assembly_formatted.btindex -f -U ../ERR599031_sample.fasta -S ERR599031_mapped.sam -p 4

# Convert SAM to BAM 
samtools view -bS ERR599031_mapped.sam > ERR599031_mapped.bam

# Sort BAM file
samtools sort ERR599031_mapped.bam -o ERR599031_mapped_sorted.bam

# Index reference and reads once again for visualization
samtools faidx ERR599031_assembly_formatted.fasta 
samtools index ERR599031_mapped_sorted.bam
```

