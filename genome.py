from locus import Locus
from contig import Contig

class Genome(Contig, Locus):

	def __init__(self, name='', size=None):
		self.Name=name
		self.Size=size
		self.Contigs=[] #init

	def addContig(self, contig):
		self.Contigs.append(contig)

	def setContigs(self,contigs):
		self.Contigs=contigs

	def addSize(self, size):
		self.Size=size

	def getSize(self):
		return self.Size

	def addName(self, name):
		self.Name=name

	def getName(self):
		return str(self.Name)

	def getContig(self, contigID):
		for item in self.Contigs:
			if item.getName() == contigID:
				return item

	def removeContig(self, contig):
		self.Contigs.remove(contig)

	def __str__(self):
		txt=''
		for contig in self.Contigs:
			string='"Name":%s,\n"Size":%s,\n"Contigs":%s\n' % (self.Name, self.Size, contig)
			txt+=string
		return txt

	def __iter__(self):
		for item in self.Contigs:
			yield item

	def getLastContig(self):
		return self.Contigs[-1]

	def readGff(self, filename):

		fh=open(filename, "r")

		for line in fh:

			##### -- ADD CONTIGS -- ####
			if line.startswith("##"):
				if line.startswith("##sequence-region"):
					line=line.split(' ')
					contig=Contig(line[1],line[3].strip())
					self.addContig(contig)
					#print contig

			#### -- ADD LOCUS TO CONTIGS -- ####
			elif line.startswith('gnl'):
				line=line.split('\t')
				contigID= line[0]
				locusID=line[-1].split(';')
				locusID=locusID[0].split('=')
				locusID=str(locusID[1])
				if "_gene" not in locusID: #filter _genes, get only CDS
					#print locusID
					#print line
					startAt=line[3]
					endsAt=line[4]
					description= str(line).split('product=')
					#description=description[1]
					#description=description.split(';')
					#description=description[0]
					if len(description) < 2:
						#print description
						description='description not found'
					else:
						description=description[1].split(';')
						description=str(description[0])

					locus=Locus(locusID, 1, startAt, endsAt, description) #TODO: ALL ALLELE NUMBERS ARE 1
					self.getContig(contigID).addLocus(locus)
				else:
					pass
				#print locus
				#print self.getContig(contigID)
				#print contigID + '\t' + str(len(self.getContig(contigID).getLocus()))
		lala=0
		for item in self.Contigs:
			lala+= int(item.getSize())
		#print lala
		self.addSize(lala)
		fh.close()

	def cleanGenome(self, listOfGenes):

		for contig in self.Contigs:
			listToKeep=[]
			for locus in contig.getLocus():
				#print locus.getName()
				if locus.getName() in listOfGenes:
					listToKeep.append(locus)
			#print 'printing list to keep '
			#print listToKeep
			contig.setLocus(listToKeep)

		contigsToKeep=[]
		for contig in self.Contigs:
			if not contig.getLocus():
				pass
			else:
				contigsToKeep.append(contig)
		#print len(contigsToKeep)
		self.setContigs(contigsToKeep)
		#print self.Contigs


	def printJason(self, outputfile, NotEnd):
		fh=open(outputfile+'.json',"a") #APPEND!
		'''
		fh.write('{')
		fh.write('"Genomes":[')
		'''
		fh.write('{')
		fh.write('"Name":"' + self.getName() + '",')
		fh.write('"Size":"' + str(self.getSize()) + '",')
		fh.write('"Contigs":[')
		for contig in self.Contigs:
			fh.write('{')
			fh.write('"Name":"' + contig.getName() + '",')
			fh.write('"Size":"' + str(contig.getSize())+'",')
			fh.write('"Locus":[')
			for locus in contig.getLocus():
				fh.write('{')
				fh.write('"Name":"'+locus.getName()+'",')
				fh.write('"AlleleNumber":"'+ str(locus.getAlleleNumber())+'",')
				fh.write('"StartAt":"'+str(locus.getStartAt())+'",')
				fh.write('"EndAt":"'+str(locus.getEndAt())+'",')
				fh.write('"Description":"'+str(locus.getDescription())+'"')
				fh.write('}')
				if locus != contig.getLastLocus():
					fh.write(',')
			fh.write(']') #end locus
			fh.write('}')
			if contig != self.getLastContig():
				fh.write(',')
		fh.write(']') #end contigs
		fh.write('}')
		'''	
		fh.write(']')	#end genomes
		fh.write('}')
		'''

		if NotEnd:
			fh.write(",")

		fh.close()

		'''import json

		coco=json.dump(self, sort_keys=True)
		print coco'''

		#coco = dict(self)

'''
lala=Genome()
lala.readGff("test.gff")
lala.addName("test")

lala.printJason("teste")
#print lala
'''



#TODO!!! ha alguma coisa errada com a formatacao das nhanhas!
