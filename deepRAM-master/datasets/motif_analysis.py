from Bio import SeqIO
from Bio import motifs
from Bio.Seq import Seq

def load_motifs(motif_file):
    # Load motifs from the XML formatted file (MEME format)
    try:
        with open(motif_file, 'r') as f:
            motif_records = motifs.parse(f, "meme")
            return list(motif_records)
    except ValueError as e:
        print(f"Error parsing motifs: {e}")
        return []

def analyze_sequences(sequences, motifs):
    results = {}
    for seq_id, sequence in sequences.items():
        seq = Seq(sequence)
        found_motifs = []
        for motif in motifs:
            # Search for motifs in the sequence
            instances = motif.instances.search(seq)
            if instances:
                found_motifs.append(motif.name)
        results[seq_id] = found_motifs
    return results

def main():
    # Path to the motif file in XML format (MEME format)
    motif_file = r"C:\Users\ranga\Desktop\Sem-3\IBS\Project ISB\deepRAM-master\motifs_database\Converted_Motif_Database.xml"
    motifs = load_motifs(motif_file)

    # Load sequences from the ChIP-seq output directory
    sequences = {}
    for record in SeqIO.parse(r"C:\\Users\\ranga\\Desktop\\Sem-3\\IBS\\Project ISB\\deepRAM-master\\datasets\\Chlp-seq out", "fasta"):


    # Analyze the sequences for motifs
     results = analyze_sequences(sequences, motifs)
    
    # Print results
    for seq_id, found_motifs in results.items():
        print(f'Sequence ID: {seq_id}, Found Motifs: {found_motifs}')

if __name__ == "__main__":
    main()
