# Y1-Sem2-Lab3
Dictionaries etccccc

1. Autumn 2018: The function below accepts a string as an input and returns a string
with the vowels removed. Rewrite the highlighted section using a list
comprehension.
def removeVowels(sentence):
  vowels = “aeiou”
  filtered_list = []
  for l in sentence:
    if l not in vowels:
    filtered_list.append(l)
  return “ “.join (filtered_list)

2. Autumn 2018: Write an iterative function hailStone that generates the hailstone
sequence of a given positive number n and prints the sequence to the screen. The
‘hailstone’ sequence starts with a positive integer and defines the next number in
the sequence as follows: if n is even, the next value is n/2. If n is odd, the next value
is 3n + 1. The sequence will converge to 1. For example, if we consider a starting
value of 10, the sequence is 10, 5, 16, 8, 4, 2, 1.

3. Summer 2019: You have been provided with the following dictionary named
hexToBinaryTable that maps a hexadecimal value to the corresponding binary value.
hexToBinaryTable = { '0':'0000', '1':'0001', '2':'0010','3':'0011', '4': '0100', '5': '0101',
'6':'0110', '7': '0111', '8': '1000 ', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D':
'1101', 'E': '1110', 'F': '1111'}
Write a function called hexToBinary(hex, d) that accepts two arguments/parameters:
a hex string to be converted to binary and the dictionary. The function should return
the binary string value. The function would be invoked as follows:
print (hexToBinary (‘ABC12’, hexToBinaryTable))
# output is 10101011110000010010

4. Summer 2019: RNA can be broken into sequences of three nucleotides (letters)
called codons, and then translated to a protein. For example, the RNA:
"AUGUUUUCU" translates to codons: "AUG", "UUU", "UCU”, which becomes a
protein with the following sequence "Methionine", "Phenylalanine", "Serine".
There are also three terminating codons (also known as 'STOP' codons); if any of
these codons are encountered, all translation ends and the protein is terminated.
For example the RNA: " AUGUUUUCUUAAAUG " translates to codons: "AUG",
"UUU", "UCU”, "UAA" and "AUG", which becomes a protein with the following
sequence "Methionine", "Phenylalanine", "Serine". This is because the stop codon 
Dr. Jason Quinlan Ó UCC 2019/20 CS1117: Introduction to Programming
“UAA” terminates the translation, so the final Methionine is translated into the
protein sequence.
Using the dictionary provided, write a function called 'proteins' that accepts a string
of RNA and the dictionary that maps the codons:
The function should generate a list of the codons making up the RNA string.
The function should then translate the codons into proteins, printing the list of
codons to screen as well as the proteins to the screen. It should terminate if a stop
codon is encountered. Show the function being invoked.
codon_map = {'AUG' : 'Methionine', 'UUU' : 'Phenylalanine', 'UUC': 'Phenylalanine',
'UUA' : 'Leucine', 'UUG' : 'Leucine', 'UCU' : 'Serine', 'UCC' : 'Serine', 'UCA' : 'Serine',
'UCG' : 'Serine', 'UAU' : 'Tyrosine', 'UAC' : 'Tyrosine', 'UGU' : 'Cysteine', 'UGC' :
'Cysteine', 'UGG' : 'Tryptophan', 'UAA' : 'stop', 'UAG' : 'stop', 'UGA' : 'stop' }
(Recall that break terminates an enclosing loop).

5. Summer 2019: Employees within a company are undertaking a health challenge to
improve their number of steps taken each day. Consider 10 employees, numbered 0
to 9, with the number of steps taken by each employee recorded over a 5 day week
with days numbered 0 to 4, in a table having 10 rows and 5 columns. Thus, for
example, the entry in row 8 and column 3 gives the number of the steps by
employee number 8 on day number 3.
Assuming that a table, stepData, has already been filled with data, write two
separate Python functions which take this table as an input parameter and return:
tenkSteps(stepData): The number of week-days on which at least 100,000 steps were made
cumulatively by all employees.
mostSteps(stepData): The number of the employee who took the most steps in the week
(assume there can only be one). You cannot use the inbuilt max or sum functions.
