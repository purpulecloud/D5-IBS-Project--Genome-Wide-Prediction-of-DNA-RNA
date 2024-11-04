import os
import gzip
import argparse

def preprocess_sequences(input_file, output_file):
    # Example preprocessing: Just copying the contents to a new file for demonstration.
    # You can replace this with actual preprocessing logic as needed.
    with open(input_file, 'r') as infile:
        with gzip.open(output_file, 'wt') as outfile:
            for line in infile:
                outfile.write(line)

def main():
    # Argument parser for command line arguments
    parser = argparse.ArgumentParser(description='Preprocess CLIP-seq sequences')
    parser.add_argument(r"C:\Users\ranga\Desktop\Sem-3\IBS\Project ISB\deepRAM-master\datasets\CLIP-seq", required=True, help='Directory containing CLIP-seq files')
    parser.add_argument(r"C:\Users\ranga\Desktop\Sem-3\IBS\Project ISB\deepRAM-master\datasets\CLIp-seq out", required=True, help='output Directory containing CLIP-seq files')
    
    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    os.makedirs(args.output_directory, exist_ok=True)

    # Loop through folders in the input directory
    for i in range(1, 32):  # Adjust the range based on your number of files (1 to 31)
        folder_name = f"{i}_filename"  # Update this if folder names are different
        folder_path = os.path.join(args.input_directory, folder_name, "30000")
        
        for sample in ['test_sample_0', 'training_sample_0']:
            sample_path = os.path.join(folder_path, sample)
            sequences_file = os.path.join(sample_path, 'sequences.fa.gz')
            
            if os.path.exists(sequences_file):
                output_file = os.path.join(args.output_directory, f"{folder_name}_{sample}_processed.gz")
                preprocess_sequences(sequences_file, output_file)
                print(f"Processed: {sequences_file} -> {output_file}")
            else:
                print(f"Sequences file not found: {sequences_file}")

if __name__ == '__main__':
    main()