# Bioinformatics projects
In this repository, all the codes formulated in my Master Thesis Degree are conserved.  has t
Each subdirectory is referring to a specific project, mandatory for the fulfillment of the course. 

# GOR-SVM directory
This project had the main intention of compare two machine learning methods as prediction method for the JPred4 protein family. 
First, a statistic analysis is performed to count the SS present in the used datasets (the JPred4 training set and the blindset).
Then, the [GOR]( https://doi.org/10.1093/bioinformatics/bti408) approach is implemented, in first place the training phase and then the prediction set. 
The SVM was launched by *thunderSVM*, using the inputs from the DSSP and FASTA files originated through the *svm_input.py* script.
Some evaluation metrics are implemented to compare the two machine learning approaches and decide which is the most efficient one, such as accuracy, TPR, FPR, SOV evaluation indexes. 
