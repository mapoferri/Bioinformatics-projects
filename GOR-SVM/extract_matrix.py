import os 
import numpy as np
import sys
#run with python3!

def extract_matrix(pssm_file):
		with open(pssm_file, "r") as pssm:
			a = 0
			matrix=[[] for line in pssm]
			with open(pssm_file, "r") as porcod:
				for line in porcod:
					line = line.split()
					#print (line)   #iterating for line
					if a == 0:            #first line (residues) 
						a += 1
						continue     #pass --> veder come funziona e sostituire in caso
					elif a >= 1 :   #cutting first line, MATRIX 
						#print (line)
						sequence_p = (line[22:42])
						print (sequence_p)
						for value in sequence_p:
							freq = np.true_divide(int(value),100)
							matrix[a].append(freq)   #normalized
						a += 1    
			#matrix_file = "matrix_"+pssm_file 
			#with open(matrix_file, "w+") as m:				
			matrix = matrix[1:len(matrix)]
				#for line in matrix:
					#m.write(str(line)+ '\n')
			return matrix
								
################################################################################
#   code to insert padding in every matrix and save to another open            #
#   extracted matrix will be used for SVM too, so we need different matrices   #
#   as GOR input (solving indexing problems)                                   #
################################################################################

#def padding(matrix):
	#padding = np.zeros((8,20), dtype = float) #empty arrays of eight rows
	#print (padding)
	#matrix = np.loadtxt(matrix, delimiter=',')
	#print (matrix)
	#gor_matrix = "gor_input_"+matrix_file
	#with open(matrix) as matrix:
	#GORMatrix = np.concatenate((padding[:,None], matrix, padding[:,None]), axis = 0)
	#GORMatrix = padding + matrix + padding #adding padding to gor input matrices	
	#print (GORMatrix)
		#with open(gor_matrix, "a+") as gor_matrix:	
				#gor_matrix.write(str(padding))
				#gor_matrix.write(str(matrix))
				#gor_matrix.write(str(padding))



if __name__ == '__main__':
	path =  sys.argv[1]                          #giving as input the directory with all files
	files_list = [f for f in os.listdir(path)]
	for files in files_list:   #iterating for file in directory
		if files.endswith('.pssm'): 
			pssm_file = files 
			matrix = extract_matrix(pssm_file)
				#gor_matrix = padding(matrix)
			#if files.startswith('matrix'):
				#matrix_file = files
				#gor_matrix = padding(matrix_file)
					#matrix_file = extract_matrix(pssm_file)
			np.save('matrix_prova_{}.npy'.format(pssm_file), matrix)
				#print (type(matrix_file))
				#gor_matrix = padding(matrix)
				#print (gor_matrix)

