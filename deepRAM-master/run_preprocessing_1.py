import os
import subprocess

# Directories for input and output
input_dir = r"C:\Users\ranga\Desktop\Sem-3\IBS\Project ISB\deepRAM-master\datasets\ChIP-seq"
output_dir = r"C:\Users\ranga\Desktop\Sem-3\IBS\Project ISB\deepRAM-master\datasets\Chlp-seq out"

for filename in os.listdir(input_dir):
    if filename.endswith('.seq.gz'):  # Process only .seq.gz files
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, 'processed_' + filename)
        subprocess.run(['python', 'preprocess_1.py', '--ENCODE_data', input_path, '--output', output_path])

