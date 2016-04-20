from matplotlib import pyplot as plt
import collections



population_dict = collections.defaultdict(int)
land_dict = collections.defaultdict(int)
with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.strip().split(',')
        line[5] = int(line[5])
        line[7] = int(line[7])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]
            land_dict[line[0]] += line[7]



print(population_dict)
print(land_dict)


for (k,v),(k2,v2) in zip(population_dict.items(),land_dict.items()):
       population_dict[k]=float(population_dict[k])/land_dict[k2]

print(population_dict)


with open('population_density.csv','w') as outputFile:
    outputFile.write('Country,Population Density \n')
    for k,v in population_dict.iteritems():
        outputFile.write(k+','+str(v)+'\n')

#plot a chart
plt.bar(range(len(population_dict)),population_dict.values(), align='center')
plt.xticks(range(len(population_dict)),population_dict.keys())
plt.title('Population Density(2010)')
plt.show()
