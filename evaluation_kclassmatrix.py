#to evaluate now we are taking in input the file containing the original sequence and the predicted sequence, identified by their ID
#ID = 'gor_input_formatted_' + id + '.pssm'
import numpy as np
#creating a matrix with 3 rows and 3 columns, with the predicted values on the columns and orginal on the rows
import os

def multi_class_evaluation(ss_original,ss_predicted):
	multi_matrix = [[0,0,0],[0,0,0],[0,0,0]]
	#print (len(ss_original))
	
	for x in range(len(ss_original)):
		
		#print (x)
		#for y in range(len(ss_predicted)):
		if ss_original[x] == 'H' and ss_predicted[x] == 'H':
							#print (ss_predicted[residue])
			multi_matrix[0][0] += 1
							#position[0][0] in the matrix
		elif ss_original[x] == 'H' and ss_predicted[x] =='E':
			multi_matrix[1][0] += 1 
		elif ss_original[x] == 'H' and ss_predicted[x] =='-':
			multi_matrix[2][0] += 1 
		elif ss_original[x] == 'E' and ss_predicted[x] =='H':
			multi_matrix[0][1] += 1
		elif ss_original[x] == 'E' and ss_predicted[x] == 'E':
			multi_matrix[1][1] += 1
		elif ss_original[x] == 'E' and ss_predicted[x] == '-':
			multi_matrix[2][1] += 1 
		elif ss_original[x] == '-' and ss_predicted[x] == 'H':
			multi_matrix[0][2] += 1 
		elif ss_original[x] == '-' and ss_predicted[x] == 'E':
			multi_matrix[1][2] += 1
		elif ss_original[x] == '-' and ss_predicted[x] == '-':
			multi_matrix[2][2] += 1
		else:
			continue
	#print (multi_matrix)
	return (multi_matrix)

def two_class_matrix_helics(final_multi_class_matrix):
	#print (final_multi_class_matrix)
	two_class_matrix = [[0,0],[0,0]]
	#correct positive
	two_class_matrix[0][0] = final_multi_class_matrix[0][0]
	#over-predictions (non-helix predicted as helix)
	two_class_matrix[0][1] = final_multi_class_matrix[0][1] + final_multi_class_matrix[0][2]
	#under-predict (helix as non-helix)
	two_class_matrix[1][0] = final_multi_class_matrix[1][0] + final_multi_class_matrix[2][0]
	#correct negative (non helix as non helix)
	two_class_matrix[1][1] = final_multi_class_matrix[1][1]+final_multi_class_matrix[1][2]+final_multi_class_matrix[2][1]+final_multi_class_matrix[2][2]
	return (two_class_matrix)


def two_class_matrix_coils(final_multi_class_matrix):
	two_class_matrix = [[0,0],[0,0]]
	#correct positive
	two_class_matrix[0][0] = final_multi_class_matrix[2][2]
	#over-prediction(non coils predicted as coils)
	two_class_matrix[0][1] = final_multi_class_matrix[2][0]+final_multi_class_matrix[2][1]
	#under-predictions (coils as non coils)
	two_class_matrix[1][0] = final_multi_class_matrix[0][2]+final_multi_class_matrix[1][2]
	#correct negative
	two_class_matrix[1][1] = final_multi_class_matrix[0][0] + final_multi_class_matrix[0][1]+final_multi_class_matrix[1][0]+ final_multi_class_matrix[1][1]
	return (two_class_matrix)

def two_class_matrix_strands(final_multi_class_matrix):
	two_class_matrix = [[0,0],[0,0]]
	#correct positive
	two_class_matrix[0][0] = final_multi_class_matrix[1][1]
	#over-predictions
	two_class_matrix[0][1] = final_multi_class_matrix[1][0]+final_multi_class_matrix[1][2]
	#under-prediction
	two_class_matrix[1][0] = final_multi_class_matrix[0][1] + final_multi_class_matrix[2][1]
	#correct negatives 
	two_class_matrix[1][1] = final_multi_class_matrix[0][0]+final_multi_class_matrix[0][2]+final_multi_class_matrix[2][0]+final_multi_class_matrix[2][2]
	#print (two_class_matrix)
	return (two_class_matrix)

def print_performance(matrix):
    tp=float(matrix[0][0]) #correct positive
    tn=float(matrix[1][1]) #correct negative
    fp=float(matrix[0][1]) #over-predictions
    fn=float(matrix[1][0]) #under-predictions
    acc=(tp+tn)/(tp+fn+tn+fp) 
    mc=((tp*tn)-(fp*fn))/(np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)))
    tpr= tp/(tp+fn) #sensitivity
    fpr= tp/(fp+tp) #ppv

    return (acc, mc, tpr, fpr)


if __name__ == '__main__':
	path = './'
	#final_multi_class_matrix = [[0,0,0],[0,0,0],[0,0,0]]
	helix_accuracy = []
	coils_accuracy = []
	strand_accuracy = []
	helix_mcc_tot = []
	coil_mcc_tot = []
	strand_mcc_tot = []
	helix_ppv_tot = []
	coil_ppv_tot = []
	strand_ppv_tot = []
	helix_sensit = []
	coils_sensit = []
	strands_sensit=[]

	for file in os.listdir(path):
		if file.endswith('.fasta'):
			dd = file.split('-')[2].split('.')[0]
			#print (dd)
			#c = file.split('-')[1]
			#g = file.split('-')[2].split('.')[0] + '.' + file.split('-')[2].split('.')[1]
			#print (c)
			#print (g)
			#if c == '2.0' and g == '0.5':
			#for i in range(1,5):
			input_file = 'predict_seq-cv-' + dd +'.fasta'
			with open(input_file) as gor_predictions:
				print(file)
				multi_class_matrix = [[0,0,0],[0,0,0],[0,0,0]]
				for line in gor_predictions:
					line = line.rstrip()
					if line.startswith('>'):
							#print (line)
						ss_original = next(gor_predictions).rstrip()
							#print (ss_original)
						ss_predicted = next(gor_predictions).rstrip()
							#print (ss_predicted)
						single_matrix = multi_class_evaluation(ss_original,ss_predicted)
						multi_class_matrix = np.add(single_matrix, multi_class_matrix)
			two_class_matrix_helix = two_class_matrix_helics(multi_class_matrix)
			two_class_matrix_coil = two_class_matrix_coils(multi_class_matrix)
			two_class_matrix_strand = two_class_matrix_strands(multi_class_matrix)	
				#gor_predictions = close(file)
			print (multi_class_matrix)
			two_class_matrix_helix = two_class_matrix_helics(multi_class_matrix)
			helix_acc, helix_mcc, helix_sen, helix_ppv = print_performance(two_class_matrix_helix)
			coil_acc, coil_mcc, coil_sen, coil_ppv = print_performance(two_class_matrix_coil)
			strand_acc, strand_mcc, strand_sen, strand_ppv = print_performance(two_class_matrix_strand)
			helix_accuracy.append(helix_acc)
			helix_mcc_tot.append(helix_mcc)
			helix_ppv_tot.append(helix_ppv)
			helix_sensit.append(helix_sen)
			coils_sensit.append(coil_sen)
			coils_accuracy.append(coil_acc)
			coil_mcc_tot.append(coil_mcc)
			coil_ppv_tot.append(coil_ppv)
			strands_sensit.append(strand_sen)
			strand_accuracy.append(strand_acc)
			strand_mcc_tot.append(strand_mcc)
			strand_ppv_tot.append(strand_ppv)
	
	helix_accuracy_media = np.mean(helix_accuracy)
	helix_accuracy_ds = np.std(helix_accuracy)
	coils_accuracy_media = np.mean(coils_accuracy)
	coils_accuracy_ds = np.std(coils_accuracy)
	strand_accuracy_media = np.mean(strand_accuracy)
	strand_accuracy_ds = np.std(strand_accuracy)
	helix_mcc_tot_m = np.mean(helix_mcc_tot)
	helix_mcc_ds = np.std(helix_mcc_tot)
	coil_mcc_tot_m = np.mean(coil_mcc_tot)
	coil_mcc_ds = np.std(coil_mcc_tot)
	strand_mcc_tot_m = np.mean(strand_mcc_tot)
	strand_mcc_ds = np.std(strand_mcc_tot)
	helix_ppv_tot_m = np.mean(helix_ppv_tot)
	helix_ppv_ds = np.std(helix_ppv_tot)
	coil_ppv_tot_m = np.mean(coil_ppv_tot)
	coil_ppv_ds = np.std(coil_ppv_tot)
	strand_ppv_tot_m= np.mean(strand_ppv_tot)
	strand_ppv_ds = np.std(strand_ppv_tot)
	helix_sens = np.mean(helix_sensit)
	helix_sens_ds = np.std(helix_sensit)
	coils_sens = np.mean(coils_sensit)
	coils_sen_ds = np.std(coils_sensit)
	strands_sens = np.mean(strands_sensit)
	strands_sens_ds = np.std(strands_sensit)


	#print (helix_accuracy, helix_accuracy_media, helix_accuracy_ds, helix_mcc_tot_m, helix_mcc_ds, helix_ppv_tot_m, helix_ppv_ds)
	#print (coils_accuracy, coils_accuracy_media, coils_accuracy_ds, coil_mcc_tot_m, coil_mcc_ds, coil_ppv_tot_m, coil_ppv_ds)
	#print (strand_accuracy, strand_accuracy_media, strand_accuracy_ds, strand_mcc_tot_m, strand_mcc_ds, strand_ppv_tot_m, strand_ppv_ds)

	print ("Helix accuracy is =", helix_accuracy_media, helix_accuracy_ds ," with MCC equal to =" , helix_mcc_tot_m, helix_mcc_ds ,"sensitivity equal =", helix_sens, helix_sens_ds, "and PPv to =", helix_ppv_tot_m, helix_ppv_ds)
	print ("Coil accuracy is =", coils_accuracy_media, coils_accuracy_ds, " with MCC equal to =" , coil_mcc_tot_m, coil_mcc_ds ,"sensitivity equal =", coils_sens, coils_sen_ds , "and PPv to =", coil_ppv_tot_m, coil_ppv_ds)
	print ("Strand accuracy is =", strand_accuracy_media, strand_accuracy_ds, " with MCC equal to =" , strand_mcc_tot_m, strand_mcc_ds ,"sensitivity equal =", strands_sens, strands_sens_ds, "and PPv to =", strand_ppv_tot_m, strand_ppv_ds)
	#print "Coil accuracy is {}, with MCC equal to {}, sensitivity equal to {} and PPv to {}".format(coils_accuracy, coil_mcc, coil_sen, coil_ppv)
	#print  "Strand accuracy is {}, with MCC equal to {}, sensitivity equal to {} and PPV to {}".format(strand_accuracy, strand_mcc, strand_sen, strand_ppv)
'''#gor_predictions = close(file)
	two_class_matrix_helix = two_class_matrix_helics(final_multi_class_matrix)
	two_class_matrix_coil = two_class_matrix_coils(final_multi_class_matrix)
	two_class_matrix_strand = two_class_matrix_strands(final_multi_class_matrix)
	helix_acc, helix_mcc, helix_sen, helix_ppv = print_performance(two_class_matrix_helix)
	coil_acc, coil_mcc, coil_sen, coil_ppv = print_performance(two_class_matrix_coil)
	strand_acc, strand_mcc, strand_sen, strand_ppv = print_performance(two_class_matrix_strand)
	print "Helix accuracy is {}, with MCC equal to {}, sensitivity equal to {} and PPv to {}".format(helix_acc, helix_mcc, helix_sen, helix_ppv)
		#print ('Helix accuracy:' helix_acc)
	print "Coil accuracy is {}, with MCC equal to {}, sensitivity equal to {} and PPv to {}".format(coil_acc, coil_mcc, coil_sen, coil_ppv)
	print  "Strand accuracy is {}, with MCC equal to {}, sensitivity equal to {} and PPV to {}".format(strand_acc, strand_mcc, strand_sen, strand_ppv)
'''