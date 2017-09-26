ssh michelsd@liverpool.its.carleton.edu

mkdir toy_dataset_directory
cd toy_dataset_directory
cp /usr/local/data/toy_datasets/toy_dataset_reads.fasta .

idba_ud -r toy_dataset_reads.fasta -o toy_assembly
cd toy_assembly

less scaffold.fa

quast.py contig-20.fa contig-40.fa contig-60.fa contig-80.fa contig-100.fa scaffold.fa –o toy_assembly_quast_evaluation 

anvi-script-reformat-fasta scaffold.fa -o toy_dataset_assembled.fa -l 0 --simplify-names

cd ~
mkdir project_directory
cd project_directory

cp /usr/local/data/Tara_datasets/Arabian_Sea/ERR598966_sample.fasta .

idba_ud -r ERR598966_sample.fasta -o ERR598966_assembly
