'''
A script to download GO files, based on project_datasets_metadata.csv.

To run:
    Launch ipython
    Type '%run download_go_data.py'
'''

import os
import pandas as pd
import requests

print("Running script to download GO functional genome annotations")
print("Pandas version: {}".format(pd.__version__))
print("Requests version: {}".format(requests.__version__))

# Directory to save files into
save_dir = "go_downloads"

print(f"Attempting to make {save_dir} directory...")
get_ipython().magic('mkdir $save_dir')

# read project metadata csv as Pandas DataFrame
meta_df = pd.read_csv('project_datasets_metadata.csv')

# strip spaces from column names
meta_df.columns = meta_df.columns.str.replace(" ", "_")

# Iterate over rows of DataFrame, retrieving and saving functional CSV 
print("Starting download...")
for row in meta_df.itertuples():
    download_url = "{}/function/GOAnnotations".format(row.Link_to_info)
    save_filename = "{}_MERGED_FASTQ_GO.csv".format(row.Run_ID)
    resp = requests.get(download_url)
    
    with open(os.path.join(save_dir, save_filename), 'wb') as f:
        f.write(resp.content)
    
    print(f"Saving '{save_filename}' to '{save_dir}'")
