from genome import Genome
from genomeList import GenomeSet as GenomeList
from geneGroup import GeneGroup

class GeneGroupCol(GeneGroup, GenomeList):

	def __init__(self, setID, GeneGroupCol=None, File2geneDic=None):

		self.ID=setID
		self.geneGroupCol=GeneGroupCol #list
		self.file2geneDic=File2geneDic #dic
		self.GenomeList=[] #list of GENOME objects

	def setGeneGroupCol(self, col):
		self.geneGroupCol=col

	def getGeneGroupCol(self):
		return self.geneGroupCol

	def setFile2GeneDic(self,dic):
		self.file2geneDic=dic

	def getFile2GeneDic(self):
		return self.file2geneDic

	def getGenomeList(self):
		return self.GenomeList

	def createColfromFiles(self, set_filename, pa_filename):
		import csv

		geneList=[]
		fileToGene={}

		#parse set file
		setfile=open(set_filename,'r')
		for line in setfile:
			line=line.replace(':','\t')
			line=line.replace('\n','')
			line=line.split('\t')
			#unique_set[line[0]]=line[1:]
			names=line[1:]
			names = [x.strip(' ') for x in names]
			geneList.append(GeneGroup(geneID=line[0].strip(), GeneList=names, nSetPresence=len(line[1:]))) #set geneID, geneList and nSetPresence for geneGroup object
		setfile.close()

		#parse presence_absence_csv file
		with open(pa_filename, 'r') as csvfile:
			reader = csv.reader(csvfile)
			header = reader.next()
			for row in reader:
				for item in geneList:
					if item.getGeneID() == row[0]:
						geneAnnotation=row[2]
						geneAnnotation=geneAnnotation.split('[')
						geneAnnotation=geneAnnotation[0].strip() #leave only the discription
						item.setAnnotation(geneAnnotation) #set Annotation
						item.setNIsolatesPresence(row[4]) #set nIsolatesPresence

		#create file dictionary ERROR! SD09 MISSING #FIXED
		filenames=header[14:] #Save file names from header row #control: all 61 here
		for gene in geneList:
			#print gene
			for item in filenames:
					genome=item.split('_')
					genome=genome[0:-1]
					#print genome
					for gene_name in gene.getGeneList():
						lala=gene_name.split('_')
						lala=lala[0:-1]
						#print lala
						if genome == lala:
							if item in fileToGene:
								fileToGene[item].append(gene_name)
							else:
								fileToGene[item]=[gene_name]

		#print fileToGene
		self.geneGroupCol=geneList
		self.file2geneDic=fileToGene

	def readGFFs(self, gffFileDir):
		import os

		listGFFdir=os.listdir(gffFileDir)
		GFFListToRead=[]
		#print listGFFdir

		#Save files for analysis in listGFFdir
		count=0
		for files in listGFFdir: #WTF maybe?
			filename=files.replace('.gff','')
			if filename in self.getFile2GeneDic().keys():
				#print filename
				#print len(self.getFile2GeneDic()[filename])
				#print filename
				#listGFFdir.remove(item)
				GFFListToRead.append(files)
		#print len(listGFFdir)
		#print GFFListToRead


		#print listGFFdir #only 30!? TODO

		#setGenomeList=GenomeList(iD=self.ID)
		setGenomeList=[]

		for item in GFFListToRead:
			path=gffFileDir+'/'+item
			filename=item.replace('.gff','')
			genome=Genome(name=filename)
			genome.readGff(path) #reads all genes in file, save in genome

			#clean genes not present in dictionary
			
			listOfGenes=self.getFile2GeneDic()[filename]

			#print listOfGenes

			genome.cleanGenome(listOfGenes) #send only the list of values for that file!
			#print genome

			setGenomeList.append(genome)

		self.GenomeList=setGenomeList

	def pringSetJson(self, outputfile):
		#TODO! Check if file already exits! if it does, remove it!!!
		fh=open(outputfile+'.json',"a")
		fh.write('{')
		fh.write('"Genomes":[')
		fh.close()
		for item in self.GenomeList:
			#item.printJason( outputfile )
			#fh=open(outputfile+'.json',"a")
			if item != self.GenomeList[-1]: #LALA
				#fh.write(';')
				item.printJason( outputfile, True) #flag - add , at the end
				#fh.write('COCO')
			else:
				item.printJason( outputfile, False)
				#print "END OF FILE"
			#fh.close()
		fh=open(outputfile+'.json',"a")
		fh.write(']}')
		fh.close()
		
	def __iter__(self):
		for item in self.geneGroupCol:
			yield item