from gene import Gene

class UniqueGene(Gene):


	def __init__(self, geneID=None, nSetPresence=None, nIsolatesPresence=None, gffFilename=None, annotation=None, geneList=None):
		self.geneID=geneID
		self.nSetPresence=nSetPresence
		self.nIsolatesPresence=nIsolatesPresence
		self.annotation=annotation

		listToUse=[]
		#Transform list into a list of Gene objects
		for item in geneList:
			gene=Gene(GeneID=str(item))  
			listToUse.append(gene)

		self.geneList=listToUse


	def appendGene(self, gene):
		self.geneList.append(gene)

	def setGeneList(self, glist):
		self.geneList=glist

	def getGeneList(self):
		return self.geneList

	def setGeneID(self,ID):
		self.geneID=ID

	def getGeneID(self):
		return self.geneID

	def setnSetPresence(self,num):
		self.nSetPresence=num

	def getnSetPresence(self):
		return self.nSetPresence

	def setNIsolatesPresence(self,num):
		self.nIsolatesPresence=num

	def getNIsolatesPresence(self):
		return self.nIsolatesPresence

	def setAnnotation(self, name):
		self.annotation=name 

	def getAnnotation(self):
		return self.annotation

	def checkIfInGeneList(self, gene):
		for item in self.geneList:
			if item == gene:
				return True
		return False

	def __iter__(self):
		for item in self.geneList:
			yield item

	def __str__(self):
		txt=''
		txt+='Gene: ' + str(self.getGeneID()) + '\n'
		txt+='Number of presences in set: ' + str(self.getnSetPresence()) + '\n'
		txt+='Number of presences in all isolates: ' + str(self.getNIsolatesPresence()) + '\n'
		txt+='Annotation: ' + str(self.getAnnotation()) + '\n'
		txt+='Gene List: '
		for item in self.getGeneList():
			txt+= str(item.strip()) + ','

		return txt