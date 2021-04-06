#GOR PREDICTION
import numpy as np
np.set_printoptions(threshold= np.inf, linewidth= 500)
import sys
import os


#first, building the information matrix, to get the log scores, used to predict the secondary structure
#compute an accuracy for the overall prediction

def gor_information(helix_mat, coils_mat, strands_mat, secondary_str, total_mat):
#for each residues log score is computed: p(residue in that position)/p(residue in total)*p(secondary structure in total)
	helix_columns = helix_mat[:,0:20]      #printing columns until the last
	coils_columns = coils_mat[:, 0:20]
	strands_columns = strands_mat[:, 0:20]
	
#INFORMATION FUNCTION - HELIX
	for row in range(0, 17):
		for column in range(0,20):
			helix_columns[row][column] = np.log(helix_columns[row][column]/(total_mat[row][column]*secondary_str[0]))
	
#INFORMATION FUNCTION - COILS
	for row in range(0,17):
		for column in range(0,20):
			coils_columns[row][column] = np.log(coils_columns[row][column]/(total_mat[row][column]*secondary_str[1]))
#INFORMATION FUNCTION -STRANDS
	for row in range(0,17):
		for column in range(0,20):
			strands_columns[row][column] = np.log(strands_columns[row][column]/(total_mat[row][column]*secondary_str[2]))

	return (helix_columns, coils_columns, strands_columns)


#prediction given the sequence profile (coming from the pssm)

def gor_prediction(helix_columns, coils_columns, strands_columns,matrix_file,sequence, ss):

	seq_predicted = ''
	probabilities = [0.0,0.0 ,0.0] #choosing the max within them and associate to a ss = [H,-,S]
	window_size = 17
	#seq_modified = (8*'-' + sequence + 8*'-') #considering the padding positions in the sequence too
	residues = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','Z']
	matrix = np.loadtxt(matrix_file, delimiter = '  ')
	#print (matrix)
	#since i have information functions results, now I can sum up the probabilities given by the initial pssm to the general ones:
	for i in range(0, len(sequence)): 
		
		W = matrix[i:i+window_size]  
	
		#character = seq_modified[i]

		for j in range(0, 17):  
			for x in range(0,20):  

				probabilities[0] += (helix_columns[j][x]*W[j][x])
				probabilities[1] += (coils_columns[j][x]*W[j][x])
				probabilities[2] += (strands_columns[j][x]*W[j][x])
				#print (np.sum(helix_columns[j][x]*W[j][x]))

		max_probability = max(probabilities)
		if max_probability == 0.0:
			seq_predicted += '?'
		elif max_probability == probabilities[0] :
			seq_predicted += 'H'
		elif max_probability == probabilities[1] :
			seq_predicted += '-'
		elif max_probability == probabilities[2]:
			seq_predicted += 'E'
		
		#print (probabilities)	
		probabilities = [0.0 ,0.0 , 0.0]
		
	print (matrix_file)
	#print (matrix_file)
	#print ('Starting one:')
	print (ss)
	#print ('Predicted sequence:')
	#print (len(seq_predicted[8:-8]))
	print (seq_predicted)
		

#Evalutation is a multi-class classification problem with 3 classes, so implementing a K-class confusion matrix, with on the columns the observed class and on the rows the predicted ones

if __name__ == '__main__':
	
	helix_freq = sys.argv[1]
	coils_freq = sys.argv[2]
	strands_freq = sys.argv[3]
	secondarystructure_freq = sys.argv[4]
	total_residues_freq = sys.argv[5]
	#for file in os.listdir("/home/mariapaola/Desktop/gor_train"):
		#if file.endswith(".npy"):
	helix_mat = np.load('helix_freq.npy')
	coils_mat = np.load('coils_freq.npy')
	strands_mat = np.load('strands_freq.npy')
	secondary_str = np.load('secondarystructure_freq.npy')
	total_mat = np.load('total_residues_freq.npy')
	helix_columns, coils_columns, strands_columns = gor_information(helix_mat, coils_mat, strands_mat, secondary_str, total_mat)

	with open("/home/mariapaola/Desktop/gor_train/jpred4.list.txt") as jpred4_list:
		for id in jpred4_list:
			id = id.rstrip()
			#print (id)
			matrix_file = "gor_input_formatted_"+id+".pssm"
			if matrix_file in os.listdir("/home/mariapaola/Desktop/gor_train"):
				#print ('Found --> ' + matrix_file)

				with open("/home/mariapaola/Desktop/gor_train/file_id_fasta_dssp.txt") as w: 
					for line in w:
						line = line.rstrip()
						if line == '>' + id:
							sequence = next(w).rstrip() #residues
							ss = next(w).rstrip() #ss
							gor_prediction(helix_columns, coils_columns, strands_columns,matrix_file, sequence, ss) 

