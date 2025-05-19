with open("C:/Users/grendes/Downloads/rosalind_revc.txt") as file:
    dna_strand = file.read().strip()

reversed_strand = dna_strand[::-1]
complementary_strand = reversed_strand.translate(str.maketrans("ATCG", "TAGC"))
print(complementary_strand)
