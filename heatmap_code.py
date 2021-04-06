#Producing Heatmaps for Gor Training Arrays
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm

helix_mat = np.load('helix_freq.npy')
coils_mat = np.load('coils_freq.npy')
strands_mat = np.load('strands_freq.npy')

helix_mat = helix_mat.transpose()
coils_mat = coils_mat.transpose()
strands_mat = strands_mat.transpose()

#20 columns
residues = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','Z']
#17 rows
window = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']

fig = plt.figure(figsize=(9,3))

bottom,top,left,right = 0.2,0.9,0.1,0.85
fig.subplots_adjust(bottom=bottom,left=left,right=right,top=top)
#plt.cm.get_cmap(name= 'Set1')
cmap_reversed = matplotlib.cm.get_cmap('summer_r')
 #for colors: summer, viridis, winter, bone
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

for ax,data in zip(fig.axes,[helix_mat,coils_mat,strands_mat]):
	p=ax.pcolor(data, cmap= cmap_reversed)
	ax.set_xticks(np.arange(len(window)))
	ax.set_yticks(np.arange(len(residues)))
	ax.set_xticklabels(window)
	ax.set_yticklabels(residues)
	plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

ax1.set_ylabel('Residues')
ax1.set_xlabel('Helices')
ax1.xaxis.set_label_position('top')
ax2.set_xlabel('Coils')
ax2.xaxis.set_label_position('top')
ax3.set_xlabel('Strands')
ax3.xaxis.set_label_position('top')
cax = fig.add_axes([right+0.05,bottom,0.03,top-bottom])
fig.colorbar(p,cax=cax)

plt.show()
'''
#SINGLE HEATMAP

fig, ax = plt.subplots()
plt.magma()
im = ax.imshow(strands_mat)
#plt.winter()

ax.set_xticks(np.arange(len(window)))
ax.set_yticks(np.arange(len(residues)))
ax.set_xticklabels(window)
ax.set_yticklabels(residues)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.colorbar(im)

#for i in range(len(window)):
	#for j in range(len(residues)):
		#text = ax.text(j, i, helix_mat[i, j], ha="center", va="center", color="w")

ax.set_title("Strands Heatmap")
fig.tight_layout()
plt.show()
'''