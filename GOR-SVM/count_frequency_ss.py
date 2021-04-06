with open("pie_plt_gor.txt", "r") as r:
    helix=0
    coil=0
    strands=0
    for i in r.read():
        if i == 'H':
            helix += 1
        elif i == 'C':
            coil += 1
        elif i == 'E':
            strands += 1
    tot = helix + coil + strands
    freq_hel = helix/tot
    freq_coil = coil/tot
    freq_strands = strands/tot
    print ('Number of Helices: %s' %helix 
            + "\n" + 'Number of Strands: %s' %strands +
            "\n" + 'Number of Coils: %s' %coil)

x = [helix, coil, strands]

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


labels = ['Helices', 'Coils', 'Strands']
colors = ['darkorange', 'firebrick', 'greenyellow']
explode = (0.08,0.05,0.05)

plt.pie(x, labels=labels, explode=explode, autopct='%1.1f%%', shadow=False, startangle=90, colors=colors, pctdistance=0.85)
centre_circle = plt.Circle((0,0), 0.70, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.tight_layout()
plt.show()

