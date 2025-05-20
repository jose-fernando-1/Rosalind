with open("C:/Users/grendes/Downloads/rosalind_rna.txt") as file:
    dna_string = file.read().strip()

rna_string = dna_string.replace("T", "U")
print(rna_string)