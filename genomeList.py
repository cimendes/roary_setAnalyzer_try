from genome import Genome

class GenomeSet(Genome):

	def __init__(self, iD):
		self.ID=iD
		self.genomeList=[] #List of Genome objects

	def addGenome(self, genome):
		self.genomeList.append(genome)

	def setGonomeList(self, GenomeList):
		self.genomeList=GenomeList

	def getLastGenome(self):
		return self.genomeList[-1]

	def __len__(self):
		return len(self.genomeList)

	def __iter__(self):
		for item in self.genomeList:
			yield item
