#SOV-evaluation: considering first segment of the structures which are
#not shorter than 4 for H and not shorter than 2 for strands.
#LAUNCH WITH PYTHON 3!
#PYTHON 2 NOT ALLOWING DECIMALS

import sys
from itertools import groupby
import numpy as np
from collections import Counter as mset

def segments(original_ss, predicted_ss, ss): 
	#dividing the predicted and the observed sequences overlapping 
	segments_original = []
	segments_predicted = []
	
	print (original_ss)
	indexes = 0
	for index, (k, g) in  enumerate (groupby(original_ss)):
		if k == ss:
			segments_original.append(list(g))
			print (segments_original)
			print (index)
			
	for k,g in groupby(predicted_ss):
		if k == ss:
			segments_predicted.append(list(g))
				
	#print (segments_original)
	#print (predicted_ss)
	#print (segments_predicted)
	#print (ss)		


	return segments_original, segments_predicted
	
def index(segments_original, segments_predicted):
	summ = []
	N = 0   #N(i) normalization value = n of residues in that conformation
	#print (segments_original)
	#print ('>', segments_predicted)
	for obs in segments_original:
		#print (obs)
		obs = mset(obs)
		#print (obs)
		counter = 0 
		for pred in segments_predicted:
			pred = mset(pred)
			intersection = obs & pred  #minov
			#rint (intersection)
			union = obs | pred #maxov 
			intersection = list(intersection.elements())
			union = list(union.elements())
			
			if intersection: #if intersection exists: 
				
				counter = 1
				N += len(list(obs.elements())) 
				#print (N) 
				minov = len(intersection)
				#print minov
				maxov = len(union)
				#print maxov
				len_obs = 1.0 * len(list(obs.elements()))
				len_pred = 1.0 * len(list(pred.elements()))
				delta = min([minov,maxov-minov, len_obs//2, len_pred//2])
				#print delta
				summ.append((minov+delta)/maxov * len_obs)
				
			else:
				N += len(obs) 
	if N != 0:
		#print (N)
		#print (summ) 
		#print (sum(summ))
		sov = 100 * (1/N) * sum(summ)
	
	elif N == 0:
		sov = 0 
	
	return (sov)

#def standard_error():
#for CV 

if __name__ == '__main__':
	ss = sys.argv[1]
	#gamma_value = sys.argv[2]
	#print('C', c_value, 'gamma', gamma_value)
	H_array = np.zeros((5), dtype=float)
	E_array = np.zeros((5), dtype=float)
	C_array = np.zeros((5), dtype=float)
	
	#print (H_array, E_array, C_array)
	#for i in range(1,6):
	
	input_filename = 'prova.txt'
	#'predict_seq-cv-' + str(i) + '.fasta'
	#print(input_filename)
	input_filepath = '/home/mariapaola/Desktop/LB2-GOR-SVM/' + input_filename
	with open(input_filepath) as prova:
			#print(prova)
			#final_sov_score = 0.0
		n_sequences = 0.0
		second = {'H':0.0, 'E':0.0, 'C':0.0}
		for line in prova: 
			if line.startswith('>'):
					#print(line, end='')
				n_sequences += 1.0
				original = next(prova).rstrip()
				predicted = next(prova).rstrip()
				#print (original)
				#print (predicted)
				#for ss in second:
						#print(type(ss))
				segments_original , segments_predicted = segments(original,predicted,ss)
				'''sov_score = index(segments_original, segments_predicted)
						#print(ss, '--->', sov_score)
					second[ss] += sov_score
			#print(second)
			#print(n_sequences)
		second['H'] = second['H']/n_sequences
		second['E'] = second['E']/n_sequences
		second['C'] = second['C']/n_sequences
		print(second)
		H_array[i] = second['H']
		E_array[i] = second['E']
		C_array[i] = second['-']
	#print(H_array)
	H_array = H_array[1:]
	#print (H_array)
	E_array = E_array[1:]
	C_array = C_array[1:]
	#print(E_array)
	#print(C_array)
	H_mean = np.mean(H_array)
	E_mean = np.mean(E_array)
	C_mean = np.mean(C_array)
	H_sd = np.std(H_array)
	E_sd = np.std(E_array)
	C_sd = np.std(C_array)
	print('Mean SOV value for Helix', '--->', H_mean, '   and standard deviation   ', H_sd)
	print('Mean SOV value for strand', '--->', E_mean, '   and standard deviation   ', E_sd)
	print('Mean SOV value for coil', '--->', C_mean, '   and standard deviation   ', C_sd)
'''
