
from GA import GA
from ReadData import ReadData
from utils import *

data = ReadData("easy_01_tsp.txt")
params = {'popSize': 100, 'noGen': 100}
ga = GA(params, data.problParams)
ga.initialisation()
ga.evaluation()
bestFitness = 0
bestDist = 0
bestChromoOverallRepres = None
for g in range(ga.getParam()['noGen']):
    ga.oneGenerationElitism()
    # ga.oneGeneration()
    # ga.oneGenerationSteadyState()
    bestChromo = ga.bestChromosome()
    if bestChromo.fitness > bestFitness:
        bestChromoOverallRepres = bestChromo.repres
        bestFitness = bestChromo.fitness
        bestDist = str(dist(bestChromo.repres, ga.getProblParam()))
    print('Best solution in generation ' + str(g) + ' is: ' +str(bestChromo.repres) + ' fitness = ' + str(bestChromo.fitness) + ' dist: ' + str(dist(bestChromo.repres,ga.getProblParam())))
print("\n")
print('Best solution overall is: ' +  str(bestChromoOverallRepres) + ' fitness = ' + str(bestFitness) + ' dist: ' + str(bestDist))

