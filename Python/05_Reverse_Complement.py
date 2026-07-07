s = input("enter a DNA sequence: ").upper()
complement = {
    "A":"T",
    "C":"G",
    "G":"C",
    "T":"A"
}
reverse_complement = ""
for n in reversed(s):
    reverse_complement += complement[n]

print(reverse_complement)
