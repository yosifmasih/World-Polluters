# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or recieved any unauthorized aid on this assignment."
#
# Name: Yosif Masih
# Section: 465, 565
# Assignment: 1b
# Date: 9/1/2021
#

import numpy as np
import matplotlib.pyplot as plt

# load the file energyconsumers.txt into a 2d array named consumers

Consumers = []

with open ('EnergyConsumers (1).txt', 'r') as nrg_consumers:
    for line in nrg_consumers.readlines():
        Consumers.append(line.split(' '))

# Using Matplotlib, create a single histogram of the consumptionfor each
# country and each year from Consumers. Create a logical bin size, and give a 
# title to the figure of your histogram.

consumers = []

for i in range(3, 45):
    
    if 'Belgium' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'France' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Germany' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Italy' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Netherlands' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Poland' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Portugal' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Romania' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Spain' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Sweden' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'United Kingdom' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Norway' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Turkey' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Kazakhstan' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Russia' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Ukraine' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Uzbekistan' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Canada' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'United States' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Argentina' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Brazil' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Chile' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Colombia' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Mexico' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Venezuela' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'China' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'India' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Indonesia' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Japan' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Malaysia' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'South Korea' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Taiwan' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Thailand' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Australia' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'New Zealand' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Algeria' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Egypt' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Nigeria' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'South Africa' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Iran' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Kuwait' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'Saudi Arabia' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
    elif 'United Arab Emirates' in Consumers[i][0]:
        Consumers[i][0] = Consumers[i][0].split('\t')
        consumers.append(Consumers[i][0])
for i in range(len(consumers)):
    consumers[i][-1] = consumers[i][-1].strip('\n')

consumers_final = []

for i in consumers:
    for values in i:
         try:
             consumers_final.append(float(values))
         except:
             pass
        
plt.figure(1)
plt.hist(consumers_final, bins = 120, range = (0,3050))
plt.xlabel('Energy consumption')
plt.title('Energy consumption of countries by year')
plt.savefig('plot_1.png')
plt.show()

# Load the file EnergyRawDataFinal.txt into any container (list, tuple, numpy 
# array, etc.) named EnergyType.

Raw = []

with open ('EnergyrawDataFinal (1).txt', 'r') as file:
    for line in file.readlines():
        Raw.append(line.split(','))
Raw.reverse()
Raw.pop()
Raw.reverse()


for i in range(len(Raw)):
    Raw[i][-1] = Raw[i][-1].strip('\n')

# Using Matplotlib, make a single creative graph comparing the Electricity and
# Natural Gas for each country and each year from EnergyType. You can create 
# any type of graph, just make sure you compare the two types of consumption.

electricity = []
gas = []
    
for i in range(len(Raw)):
    if i % 2 == 0:
        electricity.append(float(Raw[i][1]))
    else:
        gas.append(float(Raw[i][1]))
plt.figure(2)
plt.hist([electricity,gas],bins = 120, stacked=True )
plt.xlabel('Energy consumption')
plt.title('Electricity and Natural Gas consumption by country and year')
plt.legend(['Electricity','Natural Gas'])
plt.savefig('plot_2.png')
plt.show()

# Save a 2D array named Ind with all the data corresponding to the industrial 
# usage type in Consumers.

before_2000 = []
after_2000 = []

for i in range(0, len(consumers)):
    for j in range(1, 12):
        consumers[i][j] = float(consumers[i][j]) * .15
        before_2000.append(consumers[i][j])
    for l in range(12, 22):
        consumers[i][l] = float(consumers[i][l]) * .30
        after_2000.append(consumers[i][j])
    

# Using Matplotlib, create a single histogram of Ind for each country and each
# year. Make the color of the graph different for the two time periods
# (before and after 2000).       
 
plt.figure(3)
plt.hist([before_2000, after_2000],bins = 120, stacked=True )
plt.xlabel('Energy consumption')
plt.title('Industrial Energy consumption')
plt.legend(['Before the year 2000','After the year 2000'])
plt.savefig('plot_3.png')
plt.show()
# Make a histogram of the consumption for China only from Consumers.

China = []

for i in range(len(consumers)):
    if consumers[i][0] == 'China':
        China.append(consumers[i])

China[0][22] = float(China[0][22])
China[0][23] = float(China[0][23])
China[0][24] = float(China[0][24])
China[0][25] = float(China[0][25])
China[0][26] = float(China[0][26])
China[0][27] = float(China[0][27])

for i in range(1, 12):
    China[0][i] = China[0][i] / .15
for j in range(12, 28):
    China[0][i] = China[0][j] / .35
China = China[0]
China.reverse()
China.pop()
China.reverse()
  
plt.figure(4)
plt.hist(China, bins = 18)
plt.xlabel('Energy consumption')
plt.title('Energy Consumption: China')
plt.savefig('plot_4.png')
plt.show()

# Create a new numpy object array variable named Continent for usage by 
# continent data from Consumers. This variable should have the following
# categories:

eur = []
asia = []
afr = []
n_am = []
s_am = []
mid_east = []

for i in range(0, 11):
    eur.append(consumers[i])
for i in range(13, 15):
    eur.append(consumers[i])

n_am.append(consumers[16])
n_am.append(consumers[21])

for i in range(17, 21):
    s_am.append(consumers[i])
s_am.append(consumers[22])

for i in range(23, 30):
    asia.append(consumers[i])
asia.append(consumers[12])
asia.append(consumers[15])
    
for i in range(31, 34):
    afr.append(consumers[i])

for i in range(34, 36):
    mid_east.append(consumers[i])
mid_east.append(consumers[11])

# create final europe list

for i in range(len(eur)):
    eur[i].pop(0)

for i in range(len(eur)):
    for j in range(len(eur[i])):
        eur[i][j] = float(eur[i][j])

for sublist in eur:
    for i in range(0, 11):
        sublist[i] = sublist[i] * .85
    for i in range(11, 27):
        sublist[i] = sublist[i] * .65

eur_final = []

for i in range(len(eur)):
    for j in range(len(eur[i])):
        eur_final.append(eur[i][j])
        
# create final north america list

for i in range(len(n_am)):
    n_am[i].pop(0)

for i in range(len(n_am)):
    for j in range(len(n_am[i])):
        n_am[i][j] = float(n_am[i][j])

for sublist in n_am:
    for i in range(0, 11):
        sublist[i] = sublist[i] * .85
    for i in range(11, 27):
        sublist[i] = sublist[i] * .65

n_am_final = []

for i in range(len(n_am)):
    for j in range(len(n_am[i])):
        n_am_final.append(n_am[i][j])

# create final south america list

for i in range(len(s_am)):
    s_am[i].pop(0)

for i in range(len(s_am)):
    for j in range(len(s_am[i])):
        s_am[i][j] = float(s_am[i][j])

for sublist in s_am:
    for i in range(0, 11):
        sublist[i] = sublist[i] * .85
    for i in range(11, 27):
        sublist[i] = sublist[i] * .65

s_am_final = []

for i in range(len(s_am)):
    for j in range(len(s_am[i])):
        s_am_final.append(s_am[i][j])

# create final asia list

for i in range(len(asia)):
    asia[i].pop(0)

for i in range(len(asia)):
    for j in range(len(asia[i])):
        asia[i][j] = float(asia[i][j])

for sublist in asia:
    for i in range(0, 11):
        sublist[i] = sublist[i] * .85
    for i in range(11, 26):
        sublist[i] = sublist[i] * .65

asia_final = []

for i in range(len(asia)):
    for j in range(len(asia[i])):
        asia_final.append(asia[i][j])

# create final africa list

for i in range(len(afr)):
    afr[i].pop(0)

for i in range(len(afr)):
    for j in range(len(afr[i])):
        afr[i][j] = float(afr[i][j])

for sublist in afr:
    for i in range(0, 11):
        sublist[i] = sublist[i] * .85
    for i in range(11, 27):
        sublist[i] = sublist[i] * .65

afr_final = []

for i in range(len(afr)):
    for j in range(len(afr[i])):
        afr_final.append(afr[i][j])
 
# create final middle east list

for i in range(len(mid_east)):
    mid_east[i].pop(0)

for i in range(len(mid_east)):
    for j in range(len(mid_east[i])):
        mid_east[i][j] = float(mid_east[i][j])

for sublist in mid_east:
    for i in range(0, 11):
        sublist[i] = sublist[i] * .85
    for i in range(11, 27):
        sublist[i] = sublist[i] * .65

mid_east_final = []

for i in range(len(mid_east)):
    for j in range(len(mid_east[i])):
        mid_east_final.append(mid_east[i][j])
        
# Create a histogram of Continents for Only Residential usage 
# (Residential is the opposite of Industrial).

plt.figure(5)
plt.hist([eur_final, asia_final, afr_final, n_am_final, s_am_final, mid_east_final], bins = 6)
plt.legend(['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Middle East'])
plt.xlabel('Energy consumption')
plt.title('Residential Energy Consumption by Continent')
plt.savefig('plot_5.png')
plt.show()

# Load the file CarbonEmissions.txt into a list named CarbonEmissions.

CarbonEmissions = []
with open('CarbonEmissions (1).txt', 'r') as carb_em:
    for lines in carb_em.readlines():
       CarbonEmissions.append(lines.split('\t')) 

Consumers_2015 = []
Emissions = [9040.74, 4997.5, 2066.01, 1468.99, 1141.58, 729.77,585.99,  552.4, 549.23, 531.46, 450.79, 442.31, 441.91, 427.57, 389.75, 380.93, 330.75, 317.22,290.49, 282.4 , 0, 0, 0]

for i in range(len(consumers)):
    Consumers_2015.append(consumers[i][-2])
for i in range(len(Consumers_2015)):
    Consumers_2015[i] = float(Consumers_2015[i])

Consumers_2015.pop(0)
Consumers_2015.pop(1)
Consumers_2015.pop(5)
Consumers_2015.pop(8)
Consumers_2015.pop(9)
Consumers_2015.pop(10)
Consumers_2015.pop(12)
Consumers_2015.pop(14)
Consumers_2015.pop(16)
Consumers_2015.pop(17)
Consumers_2015.pop(20)
Consumers_2015.pop(22)
Consumers_2015.pop(23)

# Using a double bar graph, compare the twenty countries’ carbon emissions
# (million metric tons) from CarbonEmissions to their respective consumption
#  in Consumers for the year 2015.

plt.figure(6)
plt.bar(len(Emissions), height = Emissions[0])
plt.bar(len(Consumers_2015), height = Consumers_2015[0])
plt.legend(['Carbon emissions', 'Consumption'])
plt.title('Carbon emissions vs Energy cnsumption in the year 2015')
plt.savefig('plot_6.png')
plt.show()
# What are the countries with the highest energy usage? In what continent are
# they located? Use print() to answer this question.

print('China is the number 1 energy consumer and is in Asia.')
print('India is the number 2 energy consumer and is in Asia.')
print('The United States is the number 3 energy consumer and is in North America.')