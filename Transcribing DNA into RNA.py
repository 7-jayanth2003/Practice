dna = input("Enter DNA :").upper()
rna = " "

for n in dna:
    if n == "T":
        rna += "U"
    else:
        rna += n

print(rna)

# using replace function
# dna = input("Enter DNA :").upper()
# rna = dna.replace("T", "U")
# print(rna)