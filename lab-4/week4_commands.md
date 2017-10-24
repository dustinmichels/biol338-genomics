# Commands for Week 4

See Week 4 on [Protocals.io](https://www.protocols.io/private/fef7eaf6efeab7b2d989a7fb202baefe)

---
## Finishing up from last week

Get to folder from last week, with reads

```bash
ssh [username]@baross.its.carleton.edu
cd project_directory/
cd out/
```

Change name of contig-100.fa to conventional name for class,
Run script so that another software program (called “anvi’o") is happy,
Copy formatted, assembled file to shared class directory.

```bash
mv contig-100.fa ERR599031_assembly.fasta
anvi-script-reformat-fasta ERR599031_assembly.fasta -o ERR599031_assembly_formatted.fasta -l 0 --simplify-names
cp ERR599031_assembly_formatted.fasta /usr/local/data/class_shared
```

---
## Search for open reading frames

### Making fasta file with amino acid sequences using prodigal

Head back to toy dataset, copy assembly subsample. This is the subsample of the assembly files we made last week.

```bash
cd ~/toy_dataset_directory
cp /usr/local/data/toy_datasets/toy_dataset_assembly_subsample.fa toy_assembly
```

Run prodigal, to identify open reading frames (ORFs.)

```bash
mkdir ORF_finding
cd ORF_finding
prodigal -i ../toy_assembly/toy_dataset_assembly_subsample.fa -o toy_assembly_ORFs.gbk -a toy_assembly_ORFs.faa -p single
```

> * The `-i` flag gives the input file, which is the assembly you just made.
> * The `-o` flag gives the output file in Genbank format *The ‘-a” flag gives the output file in fasta format
> * The `-p` flag states which procedure you’re using: whether this is a single genome or a metagenome. This toy dataset is > a single genome so we are using –p single, but for your project dataset, you will use –p meta.

Take a look at the output, `less toy_assembly_ORFs.faa`.

> You should see a fasta file with amino acid sequences. Each amino acid sequence is an open reading frame (ORF), or a putative gene that has been identified from your assembly.

---
## Finding the function of our open reading frames/genes/proteins

### Do a protein blast on NCBI

1. Go to: https://blast.ncbi.nlm.nih.gov/Blast.cgi
2. Select Protein BLAST (blastp)
3. Copy sequence of first ORF into box at the top of the page.
4. Also try blasting with tblastn instead.

> *What's the difference?*  blastp is a protein-protein blast. When you run it online like this, you are comparing your protein sequence against the National Centers for Biotechnology Information (NCBI) non-redundant protein database, which is a giant database of protein sequences that is “non-redundant”—that is, each protein should be represented only once. In contrast, tblastn is a translated nucleotide blast. You are blasting your protein sequence against a translated nucleotide database. When you run it online like this, you are comparing your protein sequence against the NCBI non-redundant nucleotide database, which is a giant database of nucleotide sequnces, which can include whole genomes.

### Annotating proteins with Interproscan

> This works well for a few proteins, but it would be exhausting to do it for every single one of the thousands of proteins you will likely have in your dataset. We are going to use software called Interproscan to more efficiently and effectively annotate your proteins. It compares your open reading frames against several protein databases and looks for protein "signatures," or regions that are highly conserved among proteins, and uses that to annotate your open reading frames. It will do this for every single open reading frame in your dataset, if it can find a match.

Get rid of asterisks using sed:

```bash
sed 's/\*//g' toy_assembly_ORFs.faa > toy_assembly_ORFs.noasterisks.faa
```

Run interproscan (this can take a while):

```bash
interproscan.sh -i toy_assembly_ORFs.noasterisks.faa -f tsv
```

> * The `-i` flag gives the input file, which is your file with ORF sequences identified by Prodigal, with the asterisks removed.
> * The `-f` flag tells Interproscan that the format you want is a tab-separated vars, or “tsv,” file.

You can transfer this file to local computer using FileZilla and view it using Excel. The column headers are:

| #    | Contents                                 |
| ---- | ---------------------------------------- |
| 1.   | Protein Accession (e.g. P51587)          |
| 2.   | Sequence MD5 digest (e.g. 14086411a2cdf1c4cba63020e1622579) |
| 3.   | Sequence Length (e.g. 3418)              |
| 4.   | Analysis (e.g. database name-- Pfam / PRINTS / Gene3D) |
| 5.   | Signature Accession Number (e.g. PF09103 / G3DSA:2.40.50.140) |
| 6.   | Signature Description (e.g. BRCA2 repeat profile) |
| 7.   | Start location                           |
| 8.   | Stop location                            |
| 9.   | Score - is the e-value of the match reported by member database 9. method (e.g. 3.1E-52) |
| 10.  | Status - is the status of the match (T: true) |
| 11.  | Date - is the date of the run            |

---
## Searching for matches within your own database

Navigate to `/toy_dataset_directory/ORF_finding`

### Turn your ORF dataset into a BLAST database, using makeblastdb

```bash
makeblastdb -in toy_assembly_ORFs.faa -dbtype prot
```

> * `makeblastdb` invokes the command to make a BLAST database from your data
> * `-in` defines the file that you wish to turn into a BLAST database
> * `-dbtype`: choices are "prot" for protein and "nucl" for nucleotide

### Download FASTA seed file from pfam.org

1. Navigate to: http://pfam.xfam.org/family/PF03787. This page contains info about the RAMP proteins, "repair associated mysterious proteins" that are CRISPR-related.
2. Click on "1319 sequences" (or similar )near the top.
3. Under "format an alignment," select your format as "FASTA" from the drop-down menu, and select gaps as "No gaps (unaligned)" from the drop-down menu. Click "Generate." This generates a file, `PF03787_seed.txt`.
4. Transfer that file into toy dataset with FileZilla.

> Take a look at the Pfam file using less or using a text editing tool on the local computer. It is a FASTA file with a bunch of “seed” sequences that represent a specific protein family from different organisms.
>
> If you want to learn more about a specific sequence, you can take the first part of the fasta title (i.e. “Q2RY06_RHORT”) and go to this website: http://www.uniprot.org/uploadlists/ and paste it in the box. Then select from “UniProt KB AC/ID” to “UniProtKB” in the drop-down menu on the bottom. You will get a table with information about your protein and which organism it comes from (in this case, a type of bacterium called Rhodospirillum).

### Blast seed file against ORF file as database

```bash
blastp -query PF03787_seed.txt -db toy_assembly_ORFs.faa -evalue 1e-05 -outfmt 6 -out PF03787_vs_prodigal_ORFs_toy.blastp
```

> * `blastp` invokes the program within the blast suite that you want. (other choices are blastn, blastx, tblastn, tblastx.)
> * `-query` defines your blast query-- in this case, the Pfam seed sequences for the CRISPR RAMP proteins.
> * `-db` defines your database-- in this case, the toy assembly ORFs.
> * `-evalue` defines your maximum e-value, in this case 1x10-5
> * `-outfmt` defines the output format of your blast results. option 6 is common; you can check out https://www.ncbi.nlm.nih.gov/books/NBK279675/ for other options.
> * `-out` defines the name of your output file. I like to title mine with the general format 'query_vs_db.blastp' or something similar.

You could run the same command with a lower e-value cutoff to get different results.

```bash
blastp -query PF03787_seed.txt -db toy_assembly_ORFs.faa -evalue 1e-02 -outfmt 6 -out PF03787_vs_prodigal_ORFs_toy_evalue1e02.blastp
```

### Check results of blastp against ORF database

Transfer file to local computer with FileZilla, and open with Excel.

The columns contain the follow information:

| #    | Contents                  |
| ---- | ------------------------- |
| 1    | query sequence name       |
| 2    | database sequence name    |
| 3    | percent identity          |
| 4    | alignment length          |
| 5    | number of mismatches      |
| 6    | number of gaps            |
| 7    | query start coordinates   |
| 8    | query end coordinates     |
| 9    | subject start coordinates |
| 10   | subject end coordinates   |
| 11   | e-value                   |
| 12   | bitscore                  |

### Trying again with a different gene

1. Go to https://www.ncbi.nlm.nih.gov/protein/
2. Let’s look for the DNA polymerase from *Thermus aquaticus*, the famous DNA polymerase that is used in PCR. Type “DNA polymerase Thermus aquaticus’ in the search bar at the top.
3. Click on the first hit you get. You’ll see lots of information related to that sequence.
4. Click on “FASTA” near the top. It will give you the FASTA sequence for that protein (protein rather than DNA).
5. Copy that sequence and paste it into a new file on liverpool. Here is one way to do that: use nano to create a new file (see command). Once in nano, paste your sequence into the file. Type Ctrl+O, Enter, and then Ctrl+X.

Save FASTA protein sequence to file:

```bash
nano DNA_pol_T_aquaticus.faa
```

Blast!

```bash
blastp -query DNA_pol_T_aquaticus.faa -db toy_assembly_ORFs.faa -outfmt 6 -out DNA_pol_T_aq_vs_prodigal_ORFs_toy.blastp
```

## Applying these analyses to your project datasets

> Identify open reading frames on your project assembly using Prodigal, then determine their functions using Interproscan. Use this lab handout for reference. Don't forget to use the 'fixed' version of your contigs (the version that has been run throuh 'anvi-script-reformat-fasta.') Your TAs and I are here to help if you have questions or get stuck—usually the problem is a typo or you’re in the wrong directory, so check that first! Your Interproscan runs will take several hours, maybe days. Be sure to run them on screen so they can run overnight. In order to spread out the processes, I will ask that 6 of you start your Interproscan runs on baross, and 5 of you start your runs on liverpool. And before you start competing for one server over another, it won't matter in the long run-- all of your runs will be done by the end of the week. (I think.)

Identify open reading frames on your project assembly using Prodigal

```bash
prodigal -i ../ERR599031_assembly_formatted.fasta -o ERR599031_ORFs.gbk -a ERR599031_ORFs.faa -p meta
```

Get rid of asterisks using sed:

```bash
sed 's/\*//g' ERR599031_ORFs.faa > ERR599031_ORFs.noasterisks.faa
```

Determine their functions using Interproscan.

```bash
interproscan.sh -i ERR599031_ORFs.noasterisks.faa -f tsv
```


