import re

def find_motif_occurrences(dna: str, motif: str) -> list[int]:
    pattern = f"(?={motif})"
    return [m.start() + 1 for m in re.finditer(pattern, dna)]

with open("C:/Users/josef/Downloads/rosalind_subs (2).txt") as file:
    dna, motif = file.read().strip().split("\n")

print(*find_motif_occurrences(dna, motif), sep=" ")