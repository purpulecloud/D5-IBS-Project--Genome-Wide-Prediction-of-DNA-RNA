import os
import gzip
import argparse

def preprocess_sequences(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:  # Try UTF-8 first
            with gzip.open(output_file, 'wt') as outfile:
                for line in infile:
                    outfile.write(line)
    except UnicodeDecodeError:
        print(f"Error decoding {input_file}. Trying a different encoding...")
        try:
            with open(input_file, 'r', encoding='latin-1') as infile:  # Try Latin-1
                with gzip.open(output_file, 'wt') as outfile:
                    for line in infile:
                        outfile.write(line)
        except UnicodeDecodeError:
            print(f"Failed to decode {input_file}. Please check the file encoding.")
def main():
    # Argument parser for command line arguments
    parser = argparse.ArgumentParser(description='Preprocess CLIP-seq sequences')
    parser.add_argument("input_directory", type=str, nargs='?', default="C:\\Users\\Srikrishna\\Documents\\GitHub\\D5-IBS-Project--Genome-Wide-Prediction-of-DNA-RNA\\deepRAM-master\\datasets\\CLIP-seq\\1_PARCLIP_AGO1234_hg19\\30000", help='Directory containing CLIP-seq files')
    parser.add_argument("output_directory", type=str, nargs='?', default="C:\\Users\\Srikrishna\\Documents\\GitHub\\D5-IBS-Project--Genome-Wide-Prediction-of-DNA-RNA\\deepRAM-master\\datasets\\CLIp-seq out", help='output Directory containing CLIP-seq files')

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_directory, exist_ok=True)

    # Loop through the input directory and its subdirectories
    for root, dirs, files in os.walk(args.input_directory):
        for file in files:
            if file == 'sequences.fa.gz':
                input_file = os.path.join(root, file)
                output_file = os.path.join(args.output_directory, f"{os.path.basename(root)}_{file}")
                preprocess_sequences(input_file, output_file)
                print(f"Processed: {input_file} -> {output_file}")

if __name__ == '__main__':
    main()