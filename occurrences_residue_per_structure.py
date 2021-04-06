import pandas as pd
import matplotlib.pyplot as plt
with open("merged.txt", "r") as ids: 
    helices=[]
    coils=[]
    strands=[]
    n_residues = 0 
    for line in ids:

        if line.startswith('>') and line.endswith('\n'):
            fasta = next(ids).rstrip('\n') 
            dssp =  next(ids).rstrip('\n')
            
            for i in range(len(dssp)):
                if dssp[i] == 'E':
                    strands.append(fasta[i])
                elif dssp[i] == 'H': 
                    helices.append(fasta[i])
                elif dssp[i] == 'C':
                    coils.append(fasta[i])
        
        #if line[0].isdigit(): 
                #n_residues += int(line)
    
#    print helices


                    
                
#with open("list_of_strustures_dssp.txt", "r") as dssp:
    #dssp_file = dssp.read()
#with open("correspondence_ss_residues.txt", "a+") as correspondence: #output file, not really needed
    #for dssp_char, fasta_char in zip(dssp_file, fasta_file): comparing the two file, now only one

helixs={}
stranxs={}
coilx={}

for i in helices:
    #print i
    
    if i == 'X':
            continue
    elif i.isupper():
            if i in helixs:
                helixs[i] += 1
            else:
                helixs[i] = 1

#for value in helixs:
    #helixs[value] = float(helixs[value]/n_residues)

print (helixs)
             
for j in coils:
        if j == 'X':
                continue
        elif j.isupper():
            #print j 
            if j in coilx:
                coilx[j] += 1
            else:
                coilx[j] = 1
#for value in coilx:
    #coilx[value] = float(coilx[value]/n_residues)

print (coilx)

for z in strands:
        if z == 'X':
                continue
        elif z.isupper():
            if z in stranxs:
                stranxs[z] += 1
            else:
                stranxs[z] = 1
#for value in stranxs:
    #stranxs[value] = float(stranxs[value]/n_residues)
print (stranxs)

helix_dataframe = pd.Series(helixs)
coils_dataframe = pd.Series(coilx)
strands_dataframe = pd.Series(stranxs)
frame = {'Helices': helix_dataframe, 'Coils': coils_dataframe, 'Strands' : strands_dataframe }
results = pd.DataFrame(frame)
print (results)

results.plot.bar()
plt.title('Effective Blind Set')
plt.xlabel('Residues')
plt.ylabel('Frequency')
plt.show()

