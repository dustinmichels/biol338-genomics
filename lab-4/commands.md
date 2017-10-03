See Week 4 on [Protocals.io](https://www.protocols.io/view/week-4-calling-open-reading-frames-with-prodigal-u-js3cngn?step=4)

## Finishing up from last week

Get to folder from last week, with reads
```bash
ssh [username]@baross.its.carleton.edu
cd project_directory/
cd out/
```

Change name of contig-100.fa to conventional name for class
```
mv contig-100.fa ERR599031_assembly.fasta
```

Run script so that another software program (called “anvi’o") is happy.
```
anvi-script-reformat-fasta ERR599031_assembly.fasta -o ERR599031_assembly_formatted.fasta -l 0 --simplify-names
```

Copy formatted, assembled file to shared class directory
```
cp ERR599031_assembly_formatted.fasta /usr/local/data/class_shared
```

## Looking for open reading frames

```cp /usr/local/data/toy_datasets/toy_dataset_assembly_subsample.fa toy_assembly```





