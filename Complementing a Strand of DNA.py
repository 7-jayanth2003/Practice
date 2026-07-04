s = input("Enter a DNA string: ").upper()

reverse_s = s[::-1]
complement = ""

for n  in reverse_s:
    if n == "A":
        complement += "T"
    elif n == "T":
        complement += "A"
    elif n == "G":
        complement += "C"
    elif n == "C":
        complement += "G"

print(complement)


#1)
# s = input()
# table = str.maketrans("ATCG", "TAGC")
# print(s[::-1].translate(table))

#2)
# from Bio.Seq import Seq
# s = Seq(input())
# print(s.reverse_complement())
