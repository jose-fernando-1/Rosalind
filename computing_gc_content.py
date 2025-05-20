#atualizar path no outro pc

with open("C:/Users/josef/Downloads/rosalind_gc (1).txt") as file:
    fasta_formatted_file = file.read().strip()

strings1 = fasta_formatted_file.split(">")[1:]

fasta_dict = {}
for item in strings1:
    fasta_dict[item.split("\n")[0]] = "".join(item.split("\n")[1:])

def gc_percentage(string):
    return (string.count("G") + string.count("C")) / len(string) * 100

gc_percentages = [gc_percentage(string) for string in fasta_dict.values()]

max_label = max(fasta_dict, key=lambda k: gc_percentage(fasta_dict[k]))
max_gc = gc_percentage(fasta_dict[max_label])

print(f"{max_label}\n{max_gc}")

