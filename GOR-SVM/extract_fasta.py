import os

path = './'
files_list = [f for f in os.listdir(path)]
for file in files_list:
	id = file.rsplit('.',1)[0]
	#chain = file.rsplit('_',1)[1]
	#print (id)
	#print (chain)
	file = open(file)
	for line in file: 
		if line.startswith('>'):
			initio = line.strip()
			dssp = next(file)
			fasta=next(file).strip().upper()
			id_fasta = initio + '\n' + fasta
			#print (id_fasta)
	fasta_file = id  + '.fasta'
	with open(fasta_file, "w+") as fasta_file:
				fasta_file.write(id_fasta)
