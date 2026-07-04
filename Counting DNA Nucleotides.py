s = input("Enter a DNA string")

A = 0
C = 0
G = 0
T = 0

for n in s:
    if n == "A":
        A += 1
    elif n == "C":
        C += 1
    elif n == "G":
        G += 1
    elif n == "T":
        T += 1

print(A, C, G, T)