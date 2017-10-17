# Week 6

## Mapping with a toy dataset

### Make dir and copy files

```bash
mkdir mapping
cd mapping

cp /usr/local/data/toy_datasets/toy_dataset_reads_for_mapping.fasta .
cp /usr/local/data/toy_datasets/toy_dataset_contig_for_mapping.fasta .
```

### Prepare an index of reference with bowtie2

```bash
bowtie2-build toy_dataset_contig_for_mapping.fasta toy_dataset_contig_for_mapping.btindex
```
* bowtie2-build is the program that indexes your reference.
* The first argument gives the reference dataset name.
* The second argument provides the name you want to give to the index.

### Map, create SAM file with bowtie2

```bash
bowtie2 -x toy_dataset_contig_for_mapping.btindex -f -U toy_dataset_reads_for_mapping.fasta -S toy_dataset_mapped_species1.sam
```

* Bowtie2 is the name of the mapping program.
* “-x” is the flag that provides the name of the index you just made.
* “-f” means that the reads you are mapping are in fasta, not fastq, format.
* “-U” means that the reads are not paired.
* “-S” provides the name of your output file, which is in SAM format.

### Convert SAM file to BAM file, using samtools

```bash
samtools view -bS toy_dataset_mapped_species1.sam > toy_dataset_mapped_species1.bam
```

### Sort BAM file

```bash
samtools sort toy_dataset_mapped_species1.bam -o toy_dataset_mapped_species1_sorted.bam
```

### To visualize mapping, index reference again with samtools

```bash
samtools faidx toy_dataset_contig_for_mapping.fasta
samtools index toy_dataset_mapped_species1_sorted.bam
```

* Samtools faidx is the name of the program that indexes the reference.
* The first argument provides the name of the index, which should be your reference file.

* samtools index is the name of the program that indexes the bam files.
* The first argument provides the name of a sorted bam file.

### View with IGV

Copy fies over

```bash
scp -r [your username]@liverpool.its.carleton.edu:/Accounts/[your username]/toy_dataset_directory/mapping/ ~/Desktop
```

Using IGV:

* Click  'Genomes' --> 'Load Genome from File'
  - select 'toy_dataset_contig_for_mapping.fasta'
* Click 'File' --> 'Load from File'
  - Select 'toy_dataset_mapped_species1_sorted.bam'

See: http://software.broadinstitute.org/software/igv/AlignmentData


### Compare this mapping with another one

Back on server side...

```bash
cp /usr/local/data/toy_datasets/toy_dataset_reads_for_mapping_species2.fasta .
bowtie2 -x toy_dataset_contig_for_mapping.btindex -f -U toy_dataset_reads_for_mapping_species2.fasta -S toy_dataset_mapped_species2.sam
samtools view -bS toy_dataset_mapped_species2.sam > toy_dataset_mapped_species2.bam
samtools sort toy_dataset_mapped_species2.bam -o toy_dataset_mapped_species2_sorted.bam
samtools index toy_dataset_mapped_species2_sorted.bam
```








