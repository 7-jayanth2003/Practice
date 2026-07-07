fasta = {}

with open("05_input.fasta", "r") as file:
    current_id = ""

    for line in file:
        line = line.strip()

        if line.startswith(">"):
            current_id = line[1:]
            fasta[current_id] = ""
        else:
            fasta[current_id] += line

highest_id = ""
highest_gc = 0

for seq_id, sequence in fasta.items():
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = (gc_count / len(sequence)) * 100

    if gc_percent > highest_gc:
        highest_gc = gc_percent
        highest_id = seq_id

print(highest_id)
print(highest_gc)