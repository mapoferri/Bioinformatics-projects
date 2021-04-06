#GOR train implementation for training the model;
#starting directly from the profiles and adding the frequencies for the residue

import os
import numpy as np 
np.set_printoptions(threshold= np.inf, linewidth= 200)
#considering as input a file with all the ids, so the code itself
#needs to go and take the frequencies from the matrix!
import sys

def gor_train(matrix_file, ss, hels, coils, strands, tot_residues, secondarystructure, res): 
	#considerando matrice singole alla volta
	#initializing the matrices for windows size = 17 x 20 residues
	#8 residues before, cetral residue, 8 residues after
	#a matrix to count the incidence of the residue too 
	#a matrix to count the incidence of the ss 
	#helics, coils, strands
	#counting the residue for future normalization
	#now the problem is to find the frequency of the ss over the profiles
	matrix = np.loadtxt(matrix_file, delimiter = ',')
	window_size = 17
	#print (matrix)
	for i in range(0, len(ss)):
		#print (i)
		W = matrix[i:i+window_size]
		central_line = W[window_size//2]
		#print (W)
		#for j in range(0, matrix.shape[0]- window_size +1):
			#for k in range(0,len(matrix)):
				#W = matrix[j:j+window_size]
		if W.shape[0] == window_size:    #iterators for rows and columns
				
				if ss[i] == 'H':   #if the ss of the residue is and helix:
				#print (W[j][k])
					hels = np.add(hels, W)   #saving in the helics list in the same position the frequency from the profile
					tot_residues = np.add(tot_residues, W)
					secondarystructure[0] += 1
					if np.sum(central_line) != 0.0:
						res +=1
					else:
						continue
					#if hels[j][k] != (0.0): 
						#res += 1   #adding number with frequency to count them for normalization
					#else:
						#continue
					#print (res)

				if ss[i] == '-':
					coils = np.add(coils, W)
					#print (W)
					#print (coils)
					#coils[j][k] += W[j][k]      #adding 
					tot_residues = np.add(tot_residues, W)
					#print(tot_residues)
					secondarystructure[1] += 1
					if np.sum(central_line) != 0.0:
						res +=1
					else:
						continue
					#print (W[j][k])
					#if coils[j][k] != (0.0):
						#res += 1
					#else:
						#continue
				
				if ss[i] == 'E':
					#print (W[j][k])
					strands = np.add(strands, W)
					tot_residues = np.add(tot_residues, W)
					secondarystructure[2] += 1
					if np.sum(central_line) != 0.0:
						res +=1
					else:
						continue
					#if strands[j][k] != (0.0):
						#res += 1
					#else:
						#continue;

	
#return (hels, coils, strands, tot_residues, secondarystructure,res)
	#print (coils)
	#Normalization for n of residues: 
	normalized_hels = np.true_divide(hels, res)
	normalized_coils = np.true_divide(coils, res)
	normalized_strands = np.true_divide(strands, res)
	normalized_tot_residues = np.true_divide(tot_residues, res)
	normalized_secondarystructure = np.true_divide(secondarystructure, res)
	
	#print (matrix_file)
	#print (normalized_coils)
	return (normalized_hels, normalized_coils, normalized_strands, normalized_tot_residues, normalized_secondarystructure)

if __name__ == '__main__':
	jpred4_list = sys.argv[1]    #giving in input the list of id
	file_trainingset = sys.argv[2]
	#matrix_file = sys.argv[1]
	hels = np.zeros((17,20), dtype = float) #17 rows and 20 columns
	coils = np.zeros((17,20), dtype = float)
	strands = np.zeros((17,20), dtype = float)
	tot_residues = np.zeros((17,20), dtype = float)
	secondarystructure = [0.0, 0.0, 0.0]
	res = 0
	final_hels = np.zeros((17,20), dtype = float) #17 rows and 20 columns
	final_coils = np.zeros((17,20), dtype = float)
	final_strands = np.zeros((17,20), dtype = float)
	final_tot_residues = np.zeros((17,20), dtype = float)
	final_secondarystructure = [0.0, 0.0, 0.0]
	#input the sequence file with ids
	with open(jpred4_list) as jpred4_list:
		for id in jpred4_list:
			id = id.rstrip()
			#print (id)
			matrix_file = "gor_input_"+id+".pssm"
			if matrix_file in os.listdir("/home/mariapaola/Desktop/gor prova"):
				print(matrix_file)
				#print (id)
				with open(file_trainingset) as w: 
					for line in w:
						line = line.rstrip()
						if line == '>' + id:
							sequence = next(w).rstrip() #residues
							ss = next(w).rstrip() #ss  
							print (line + '\n'+ sequence +'\n' + ss)
						    
							normalized_hels, normalized_coils, normalized_strands, normalized_tot_residues, normalized_secondarystructure = gor_train(matrix_file ,ss,hels, coils, strands, tot_residues, secondarystructure, res )
							#print (coils)
							print (normalized_coils)
							
						else:
							continue
			else:
				continue

		#np.save('helix_freq.npy', normalized_hels)
		#np.save('coils_freq.npy', normalized_coils)
		#np.save('strands_freq.npy', normalized_strands)
		#np.save('total_residues_freq.npy', normalized_tot_residues)
		#np.save('secondarystructure_freq.npy', normalized_secondarystructure)
		
