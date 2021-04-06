import os
import numpy as np 
np.set_printoptions(threshold= np.inf, linewidth= 500)
import sys

def svm_input(pssm_file, ss):
	matrix = np.load(pssm_file)
	window_size = 17
	#print (ss)
	feature_arr = np.zeros((1,340), dtype =float)
	class_arr = np.zeros((1,1,), dtype=int)
	for i in range(0, len(ss)):
		W = matrix[i:i+window_size]
		W = W.flatten()
		#feature_arr = np.concatenate((feature_arr, [W]), axis = 0)
		
		if W.sum() != 0.0:

			feature_arr = np.concatenate((feature_arr, [W]), axis = 0)
		
			if ss[i] == 'H':
				class_arr = np.concatenate((class_arr, [[1]]), axis = 0)
			elif ss[i] == 'E':
				class_arr = np.concatenate((class_arr, [[2]]), axis = 0)
			elif ss[i] == '-':
				class_arr = np.concatenate((class_arr, [[3]]), axis = 0)
		#print (class_arr.flatten())
		else:
			print('>')
			#continue 
	
	feature_arr = np.delete(feature_arr,0,0)
	class_arr = np.delete(class_arr,0,0)
	#class_arr = class_arr.flatten()
	#feature_arr = feature_arr.flatten()
	#print (feature_arr)
	#print (class_arr)
	#print (class_arr.flatten())
	return (feature_arr, class_arr)


if __name__ == '__main__':
	dssp_directory = sys.argv[1]
	#dssp files with identifier and sequence after
	#/home/mariapaola/Desktop/LB2-GOR-SVM/cv/dssp/
	pssm_directory = sys.argv[2]
	#using numpy arrays used for input gor too
	#/home/mariapaola/Desktop/LB2-GOR-SVM/cv/pssm/
	training_id_input = sys.argv[3]
	#list of ids with identifiers
	feature_array = np.zeros((1,340), dtype=float)
	class_array = np.zeros((1,1,), dtype=int)
	with open(training_id_input) as ids:
		for id in ids:
			id = id.rstrip()
			#print (id)
			dssp_file = id + ".dssp"
			#print (dssp_file)
			pssm_file = "gor_input_matrix_"+id+".npy"
			#print (pssm_file)
			if pssm_file in os.listdir(pssm_directory):
				#print (pssm_file)
				pssm_file = pssm_directory + pssm_file
				if dssp_file in os.listdir(dssp_directory):
					#print (dssp_file)
					dssp = dssp_directory + dssp_file
					with open(dssp) as dssp:
						for line in dssp:
							if line.startswith('>'):
								ss = next(dssp).rstrip()
								feature_arr , class_arr = svm_input(pssm_file,ss)
								#print (id)
								feature_array = np.concatenate((feature_array, feature_arr), axis = 0)
								class_array = np.concatenate((class_array, class_arr), axis = 0)
		feature_array = np.delete(feature_array,0,0)
		class_array = np.delete(class_array,0,0)
		#np.save('feature_all_cv.npy', feature_array)
		class_array = class_array.flatten()
		#print (len(feature_array))
		#print (len(class_array))
		#np.save('class_all_cv.npy', class_array)
