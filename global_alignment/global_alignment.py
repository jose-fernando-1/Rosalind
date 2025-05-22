from needleman_wunsch_folder.needleman_wunsch import needleman_wunsch

dna1 = "GATATATGCATATACTT"
dna2 = "AGATATACGCAATACTTG"

alignment1, alignment2, score = needleman_wunsch(dna1, dna2)
print(alignment1)
print(alignment2)
print(score)