import os
import pandas as pd

input_folder = 'deepRAM-master\\datasets\\CLIp-seq out\\seq files' 
output_fasta_folder = 'deepRAM-master\\datasets\\CLIp-seq out\\CLIp-seq fasta' 
output_label_folder = 'deepRAM-master\\datasets\\CLIp-seq out\\CLIp-seq label' 

# Ensure output directories exist
os.makedirs(output_fasta_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)

# Process each RNA file in the input folder
for file_name in os.listdir(input_folder):
    input_file_path = os.path.join(input_folder, file_name)
    rna_data = pd.read_csv(input_file_path, sep="\t", header=None)    
    sequences = rna_data.iloc[1:, 0]  
    labels = rna_data.iloc[1:, 1]
    base_name = os.path.splitext(file_name)[0]
    fasta_file_path = os.path.join(output_fasta_folder, f"{base_name}.fasta")
    label_file_path = os.path.join(output_label_folder, f"{base_name}_labels.txt")
    with open(fasta_file_path, 'w') as fasta_file:
        for idx, sequence in enumerate(sequences, start=1):
            fasta_file.write(f">Sequence_{idx}\n{sequence}\n")
    labels.to_csv(label_file_path, index=False, header=False)

print("Processing completed. Check the output folders for results.")