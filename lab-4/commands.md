See Week 4 on [Protocals.io](https://www.protocols.io/view/week-4-calling-open-reading-frames-with-prodigal-u-js3cngn?step=4)

## Finishing up from last week

1. Get to folder from last week, with reads
```bash
ssh [username]@baross.its.carleton.edu
cd project_directory/
cd out/
```

2. change name of contig-100.fa to conventional name for class
```
mv contig-100.fa ERR599031_assembly.fasta
```

3. run script so that another software program (called “anvi’o") is happy.
```
anvi-script-reformat-fasta ERR599031_assembly.fasta -o ERR599031_assembly_formatted.fasta -l 0 --simplify-names
```

4. copy formatted, assembled file to shared class directory
```
cp ERR599031_assembly_formatted.fasta /usr/local/data/class_shared
```

5. Looking for open reading frames



