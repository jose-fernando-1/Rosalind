dna_codon_dictionary = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': 'Stop', 'TAG': 'Stop',
    'TGT': 'C', 'TGC': 'C', 'TGA': 'Stop', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

stop_codons = {'TAA', 'TAG', 'TGA'}

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def translate(dna):
    protein = ''
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        amino = dna_codon_dictionary.get(codon, '')
        if amino == 'Stop':
            break
        protein += amino
    return protein

def find_orfs_in_frame(dna):
    proteins = set()
    for i in range(len(dna) - 2):
        codon = dna[i:i+3]
        if codon == 'ATG':
            for j in range(i, len(dna)-2, 3):
                next_codon = dna[j:j+3]
                if next_codon in stop_codons:
                    orf = dna[i:j+3]
                    protein = translate(orf)
                    if protein:
                        proteins.add(protein)
                    break
    return proteins

def get_all_orfs(dna):
    proteins = set()
    strands = [dna, reverse_complement(dna)]
    for strand in strands:
        for frame in range(3):
            frame_seq = strand[frame:]
            proteins.update(find_orfs_in_frame(frame_seq))
    return proteins

def parse_fasta(filename):
    with open(filename) as f:
        lines = f.readlines()
        return ''.join(line.strip() for line in lines if not line.startswith('>'))

dna = parse_fasta("rosalind_orf.fasta")
proteins = get_all_orfs(dna)
print(*proteins, sep='\n')
