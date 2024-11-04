import argparse
import gzip
import csv
import random

def dinucshuffle(sequence):
    b = [sequence[i:i+2] for i in range(0, len(sequence), 2)]
    random.shuffle(b)
    d = ''.join([str(x) for x in b])
    return d

def convert_format(args):
    ENCODE_data = args.ENCODE_data
    output = args.output
    
    with gzip.open(output, 'wb') as fw:
        fw.write('sequence\tlabel\n'.encode('utf-8'))
        with gzip.open(ENCODE_data, 'rt') as data:
            next(data)
            reader = csv.reader(data, delimiter='\t')
            for row in reader:
                fw.write(row[2].encode('utf-8'))
                fw.write('\t'.encode('utf-8'))
                fw.write('1'.encode('utf-8'))
                fw.write('\n'.encode('utf-8'))
                
                # Writing shuffled sequence with label 0
                fw.write(dinucshuffle(row[2]).encode('utf-8'))
                fw.write('\t'.encode('utf-8'))
                fw.write('0'.encode('utf-8'))
                fw.write('\n'.encode('utf-8'))

def parse_arguments():
    parser = argparse.ArgumentParser(description='Preprocessing ChIP-seq file')
    
    # Data arguments
    parser.add_argument('--ENCODE_data', type=str, 
                     default = 'C:\\Users\\ranga\\Desktop\\Sem-3\\IBS\\Project ISB\\deepRAM-master\\datasets',
                    help='Path for ENCODE ChIP-seq data')
    
    parser.add_argument('--output', type=str, default='train_ChIP.gz',
                        help='Path for output file that matches format needed for deepRAM')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    convert_format(args)
