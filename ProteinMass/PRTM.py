'''
Given: A protein string PP of length at most 1000 aa.

Return: The total weight of PP. Consult the monoisotopic mass table.
'''

def weight(protein):
	# Build mass table from mass_table.txt
	mass = {}
	with open("mass_table.txt", "r") as m:
		for line in m:
			lst = line.split("   ")
			mass[lst[0]] = float(lst[1].rstrip())

	# Calculate the mass of protein
	total = 0
	for aa in protein:
		total += mass[aa]

	return total
