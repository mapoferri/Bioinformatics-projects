import sys
import os
import numpy as np 

def padding(matrix_file):
	#matrix_file = matrix_file.astype(float)
	matrix_file = np.load(matrix_file)
	#matrix = np.array(matrix_file)
	#print (matrix_file)
	padding = np.zeros((8,20), dtype = float) #empty arrays of eight rows
	
	gor_input = np.concatenate((padding,matrix_file,padding), axis =0)
	return gor_input

if __name__ == '__main__':
	path =  sys.argv[1]                          #giving as input the directory with all files
	files_list = [f for f in os.listdir(path)]
	for file in files_list: 
		if file.endswith('.npy'):
			matrix_file = file
			gor_input = padding(matrix_file)
			np.save('gor_input_{}.npy'.format(matrix_file), gor_input)
