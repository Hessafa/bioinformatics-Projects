from Bio import SeqIO
from Bio.SeqUtils import gc

def analyze_sequence(file_path):
    record = SeqIO.read(file_path, "fasta")
    sequence = record.seq

    print(f"Sequence ID: {record.id}")
    print(f"Sequence Length: {len(sequence)}")
    print(f"GC Content: {gc(sequence):.2f}%")
    print(f"Reverse Complement: {sequence.reverse_complement()}")
    print(f"Nucleotide Counts: {dict((nt, sequence.count(nt)) for nt in 'ATGC')}")

if __name__ == "__main__":
    analyze_sequence("example.fasta")
