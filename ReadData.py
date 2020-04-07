
import Chromosome
from utils import functionFitness
class ReadData:
    problParams={}
    def __init__(self, filename):
        self.__filename = filename
        self.__problParams = self.readFromFile()

    @property
    def problParams(self):
        return self.__problParams
    def readFromFile(self):

        file=open(self.__filename,"r")
        graph=[]
        noNodes=int(file.readline())
        for line in file:
            costs=line.split(",")
            chromosome=[]
            for cost in costs:
                chromosome.append(int(cost))
            graph.append(chromosome)
        problParams = {"noNodes":noNodes,
                       "graph":graph,
                       "functionFitness":functionFitness}

        return problParams
        

