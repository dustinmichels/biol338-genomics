
# coding: utf-8

# # Extract Proteins from Blastp

# A blastp returned a list of contigs that matched known 16s rRNA proteins. To create a phylogenetic tree, I had to determine the protein sequence of these contigs, by looking back to the ORF file. This script creates a FASTA file with the protein sequences of the contigs in the blast file.

# In[1]:


# import pandas, a data-wrangling library
import pandas as pd
from Bio import SeqIO
import textwrap


# ### I. Make pandas dataframe from blastp file

# In[2]:


blastp_file = "16s_protein_vs_ERR599031_ORFs.blastp"

blastp_headers = ["query_seq_name",
                  "db_seq_name",
                  "percent_identity",
                  "alignment_len",
                  "num_mismatches",
                  "num_gaps",
                  "query_start",
                  "query_end",
                  "subject_start",
                  "subject_end",
                  "e-value",
                  "bitscore"]

blastp_df = pd.read_csv(
    blastp_file, header=None,
    delimiter="\t", names=blastp_headers)


# In[3]:


# Sort by evalue
blastp_df.sort_values('e-value', inplace=True)


# In[4]:


# head() displays the first n rows of the dataframe
blastp_df.head(n=10)


# ### Find protein sequences in ORF file, to create FASTA file

# In[5]:


ORF_file = "ERR599031_ORFs.faa"
outfile = "16s_ORF_project.fasta"


# In[6]:


# Use biopython to parse full ORF file
fasta_sequences = SeqIO.parse(open(ORF_file),'fasta')


# In[7]:


# Iterate over entries in ORF fasta file,
# writing to new file any entry contained in blast file

with open(outfile, 'w') as file:
    
    for fasta in fasta_sequences:
        if blastp_df['db_seq_name'].str.contains(fasta.id).any():
            print(">" + fasta.id)
            file.write("\n>" + fasta.id + "\n")

            print(textwrap.fill(str(fasta.seq), width=60))
            file.write(textwrap.fill(str(fasta.seq), width=60))


# In[ ]:




