import os
path = './'
files_list = [f for f in os.listdir(path)]
for fildssp in files_list:
    with open(fildssp, 'r') as s:
        line = s.readline()
        if line.startswith('>'):
        	nextLine = next(s)
        	residues = nextLine.strip()
    with open("list_of_strustures.txt","a+") as r:
        r.write(residues)
        
