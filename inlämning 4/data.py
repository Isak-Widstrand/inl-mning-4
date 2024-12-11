import csv
import numpy as np
import matplotlib.pyplot as plt

#A

#Funktion för att läsa filen tempdata
def read_csv_to_list(filename):
    with open (filename, 'r') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader: 
            rows.append(row)
        return rows

#Omvandlar värdena i listan rows till float, tar bort första värdet(rubriken)
def get_kolumn_as_float(rows, kolumn_index):
    kolumn = []
    for row in rows [1: ]:
        kolumn.append(float(row[kolumn_index]))
    return kolumn

rows = read_csv_to_list('tempdata.csv')
x =  get_kolumn_as_float(rows,0)
y = get_kolumn_as_float(rows,3)
a_delare = len(x)
a_total = sum(y)
totpermv = a_total/a_delare
print (f'Medeltemperaturen för hela tidsperioden var {totpermv:.2f} grader.')

#B

#Skapar en dict och lägger in år som nycklar och en lista med temp som värden
arsdata = {}
for rad in rows[1:]:
        ar = float(rad[0])
        temperatur = float (rad[3])
        if ar not in arsdata:
            arsdata[ar] = []
        arsdata[ar].append(temperatur)

#går igenom arsdata och lägger lägger in årtalet och dess medelvärde i en lista
arsmedelvarden = []
for ar, temperaturer in arsdata.items():
    arsmedelvarde = sum(temperaturer)/len(temperaturer)
    arsmedelvarden.append([ar, arsmedelvarde])

#skippar sista värdet i listan
arsmedelvarden = arsmedelvarden [:-1]
xaxel = [year[0] for year in arsmedelvarden]
yaxel= [medel[1] for medel in arsmedelvarden]

#skapar en csv fil
with open ('arsmedelvarden.csv', 'w', newline='') as c:
    skriv = csv.writer(c)
    skriv.writerow(['År', 'Årsmedelvarden'])
    skriv.writerows(arsmedelvarden)

plt.bar(xaxel, yaxel)
plt.show()

#C

#Funk beräknar n-årsmedevärde, tar in årsmedelvärden från B, medeltemp för hela perioden från del A
def berakna_n_ars_medelvarden(arsmedelvarden, n, totpermv):
    resultat = []
    for aret in range(len(arsmedelvarden)):
        ar = arsmedelvarden[aret][0]
        start = max(0, aret - n // 2)
        slut = min(len(arsmedelvarden), aret + n // 2 + 1)
        lokalt_medel = sum([arsmedelvarden[temperatur][1] for temperatur in range(start, slut)]) / (slut - start)
        resultat.append((ar, lokalt_medel - totpermv))  
    return resultat

n = 30
n_ars_medel = berakna_n_ars_medelvarden(arsmedelvarden, n, totpermv)

n_xaxel = [ar[0] for ar in n_ars_medel]
n_yaxel = [temp[1] for temp in n_ars_medel]
plt.bar(n_xaxel, n_yaxel)
plt.show()
