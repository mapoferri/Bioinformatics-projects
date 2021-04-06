
import os

path = './'
files_list = [f for f in os.listdir(path)]
dssp_ids=[]
for feli in files_list:
	if feli.endswith('.dssp'):
		dssp_file = feli
		#print(dssp_file)
		dssp_id = dssp_file.rsplit('.',1)[0]
		dssp_ids.append(dssp_id)
		#print (dssp_file)
		#print (dssp_id)	
print(dssp_ids)

with open("150random.txt","r") as ids:
	for line in ids: 
		pdb_id = line.split('_',1)[0]
		chain_id = line.split('_',1)[1].strip()
		#print (pdb_id)
		#print (chain_id)
		if pdb_id in dssp_ids:
			#print (pdb_id)
			#chain = (pdb_id.split(" ",2)[1])
			c=0
			dssp_file = path + pdb_id + '.dssp'
			dssp=[]
			#print (dssp_file)
			not_useful_ss_file = []
			fasta_sequence = ''   #string to save the fasta
			
			ss_sequence = ''
			#print (dssp_file)
			with open(dssp_file, "r") as r:
				for line in r:
					#print(line)
					if line.find("#  RESIDUE")==2:
						#print('True')
						c=1
						continue
					if c==0:
						continue
					if line[13]=='!':
						continue
					#if '!*' in line: separatore di catena
					if line[11] == chain_id :
						residue = line[13]
						fasta_sequence = fasta_sequence + str(residue)
						chain = line[11]
						ss = line[16]
						#print (ss)
						#ss_sequence = ss_sequence + str(ss)
						inutile = line[5:10]
						total = [ chain, residue, ss]
						if residue == '!':
							not_useful_ss_file.append(total)    #eliminating the file with rsidues not specified
						else:
							dssp.append(total)
						#print(('\n'.join(' '.join(map(str,sl)) for sl in dssp)), end='')
						#for s in dssp:
						#print (ss_sequence)
							#print (s, end=' ')
					ss_res = total[2]
					ss_sequence = ss_sequence + str(ss_res)

			#print (pdb_id + '_' + chain + '\n' + fasta_sequence)
			ss_file = pdb_id + '_' + chain_id + '_ss'  + '.dssp'
			#fasta_file = pdb_id + "_" + chain_id + '.fasta'
			with open(ss_file, "w+") as ss_file:
				ss_file.write(ss_sequence)
						#print (dssp)
