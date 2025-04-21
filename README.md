# 🧬 DNA Sequence Analyzer🧬

This is a beginner-friendly bioinformatics tool that analyzes DNA sequences from FASTA files using Python and Biopython.

## Features
- Load DNA from a FASTA file
- Calculate:
  - Sequence length
  - GC content
  - Reverse complement
  - Nucleotide counts

##  How to Run

1. Install requirements:
```bash
pip install -r requirements.txt
```
---


### How the DNA Sequence Analyzer Works

Here’s how the DNA Sequence Analyzer processes the data:

1. **Load the FASTA File**:
    - The script reads the `example.fasta` file using Biopython's `SeqIO.read()` function.
    - The file contains a header (e.g., `>ExampleSequence`) followed by a DNA sequence (e.g., `ATGCGTACGTTAGCTAG...`).
2. **Extract Key Sequence Information**:
Once the sequence is loaded, the script performs the following steps:
    - **Sequence ID**: Extracts the identifier from the FASTA file (e.g., `ExampleSequence`).
    - **Sequence Length**: Calculates the total length of the DNA sequence.
    - **GC Content**: Calculates the percentage of guanine (G) and cytosine (C) nucleotides in the sequence:
        - Formula: `GC Content = (G + C) / Total Sequence Length * 100`.
    - **Reverse Complement**: Generates the reverse complement of the DNA sequence (e.g., changing `A` to `T`, `C` to `G`).
    - **Nucleotide Counts**: Counts how many times each nucleotide (A, T, G, C) appears in the sequence.
3. **Display Results**:
After processing the sequence, the script prints the following information:
    - **Sequence ID**
    - **Sequence Length**
    - **GC Content**
    - **Reverse Complement**
    - **Nucleotide Counts (A, T, G, C)**

This process allows you to quickly analyze a DNA sequence and retrieve essential information about its composition.
