# -*- coding: utf-8 -*-
"""highlightnucleotide.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wYiuKcDANz31O8tPDurYTWwCftuVkX-E
"""

from Bio import SeqIO

# Input del archivo FASTA
fasta_file = input("Insert the path of the FASTA file to scan: ")

try:
    # Leer la secuencia del archivo FASTA
    with open(fasta_file, "r") as file:
        record = next(SeqIO.parse(file, "fasta"))  # Tomar solo la primera secuencia
        adn_seq = str(record.seq).upper()  # Convertir la secuencia a mayúsculas

    # Validar la secuencia de ADN
    if not all(base in "ATGC" for base in adn_seq):
        print("Error: DNA sequence contains invalid characters.")
    else:
        # Dividir la secuencia en codones
        codons = [adn_seq[i:i+3] for i in range(0, len(adn_seq), 3) if len(adn_seq[i:i+3]) == 3]

        # Input del codón de interés
        interest_codon = input("Insert codon to identify (3 nucleotides): ").upper()

        # Validar el codón de interés
        if len(interest_codon) != 3 or not all(base in "ATGC" for base in interest_codon):
            print("Error: Codon must be exactly 3 nucleotides (A, T, G, C).")
        else:
            # Contar las ocurrencias del codón
            codon_count = codons.count(interest_codon)

            # Resaltar el codón de interés
            highlighted_seq = "".join(
                f"-[{codon}]-" if codon == interest_codon else codon
                for codon in codons
            )

            # Mostrar resultados
            print("\nHere is the nucleotide sequence you are looking for:")
            print(highlighted_seq)
            print(f"\nThe codon '{interest_codon}' appears {codon_count} times.")

except FileNotFoundError:
    print("Error: The specified FASTA file does not exist.")
except StopIteration:
    print("Error: The FASTA file does not contain any sequences.")