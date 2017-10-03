# Get to folder from last week, with reads
ssh [username]@baross.its.carleton.edu
cd project_directory/
cd out/

# change name of contig-100.fa to conventional name for class
mv contig-100.fa ERR599031_assembly.fasta

# run script so that another software program (called “anvi’o") is happy.
anvi-script-reformat-fasta ERR599031_assembly.fasta -o ERR599031_assembly_formatted.fasta -l 0 --simplify-names

# copy formatted, assembled file to shared class directory
cp ERR599031_assembly_formatted.fasta /usr/local/data/class_shared

# Looking for open reading frames



