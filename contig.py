from locus import Locus

class Contig(Locus):

	def __init__(self, name='', size=None):
		self.Name=name
		self.Size=size
		self.Locus=[]

	def addLocus(self, locus):
		self.Locus.append(locus)

	def getLocus(self):
		return self.Locus

	def setLocus(self, locus):
		self.Locus=locus

	def getName(self):
		return str(self.Name)

	def getSize(self):
		return self.Size

	def __str__(self):
		txt=''
		for locus in self.Locus:
			string='"Name":%s,\n"Size":%s,\n"Locus":%s\n' % (self.Name, self.Size, locus)
			txt+=string
		return txt

	def __iter__(self):
		for item in self.Locus:
			yield item

	def getLastLocus(self):
		return self.Locus[-1]
		