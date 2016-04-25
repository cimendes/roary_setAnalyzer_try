'''
Version 0.1
Inês Mendes
'''

from geneGroupCol import GeneGroupCol


#TODO! verify if file exists

def main():
	gffpath='/home/ines/Dropbox/Tese/roary/gff_roary'

	setOne='/home/ines/Dropbox/Tese/roary/roary_ines_n61/set_difference_unique_set_one'
	setTwo='/home/ines/Dropbox/Tese/roary/roary_ines_n61/set_difference_unique_set_two'

	pa_file='/home/ines/Dropbox/Tese/roary/roary_ines_n61/gene_presence_absence.csv'

	col_setOne=GeneGroupCol(setID="SetOne")
	col_setOne.createColfromFiles(setOne, pa_file)

	col_setOne.readGFFs(gffpath) #TODO

	print len(col_setOne.getGenomeList())

	col_setOne.pringSetJson('set_One')



	col_setTwo=GeneGroupCol(setID="SetTwo")
	col_setTwo.createColfromFiles(setTwo, pa_file)

	col_setTwo.readGFFs(gffpath) #TODO

	print len(col_setTwo.getGenomeList())

	col_setTwo.pringSetJson('set_Two')


	#print col_setOne.getGeneGroupCol()[1]
	#print col_setOne.getFile2GeneDic()



if __name__ == "__main__":
	main()