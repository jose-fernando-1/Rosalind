with open("C:/Users/grendes/Downloads/rosalind_dna (3).txt") as file:
    dna = file.read().strip()

print(f"{dna.count('A')} {dna.count('C')} {dna.count('G')} {dna.count('T')}")