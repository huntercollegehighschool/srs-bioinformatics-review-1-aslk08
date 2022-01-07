"""
Feel free to modify the dna elements to try different DNA strings
"""

import os

part = int(input("Which part(A, B, C, D, E)?")).upper()

while part not in ['A', 'B', 'C', 'D', 'E']:
  os.system('clear')
  print("That's not a valid part.")
  part = int(input("Which part(A, B, C, D, E)?")).upper()

os.system('clear')

dna = ["ACTGAAAGTG", "CTGAAAGT", "GGAAAGCC" "TTAACCGAAAG", "ACD"]

if part == "A":
  from Antcheck import isDNA
  for sequence in dna:
    print(sequence, "valid?", isDNA(sequence))

elif part == "B":
  from Bntcount import ntcount
  for sequence in dna:
    print(sequence, "counts:", ntcount(sequence))

elif part == "C":
  from Ccomplement import reversecomplement
  for sequence in dna:
    print(sequence, "reverse complement:", reversecomplement(sequence))

elif part == "D":
  from Ddnahamming import hammingdistance
  for i in range(len(dna)-1):
    print(dna[i], dna[i+1], "Hamming count:", hammingdistance(dna[i], dna[i+1]))

elif part == "E":
  from Ecommonsubstring import commonsubstring
  print("Common substring:", commonsubstring(dna[:-1]))