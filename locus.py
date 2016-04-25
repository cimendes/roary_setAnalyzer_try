class Locus:

	def __init__(self, name='', alleleNumber=1, startAt=None, endAt=None, description=None):
		self.Name=name
		self.AlleleNumber=alleleNumber
		self.StartAt=startAt
		self.EndAt=endAt
		self.Description = description

	def getName(self):
		return self.Name

	def getAlleleNumber(self):
		return self.AlleleNumber

	def getStartAt(self):
		return self.StartAt

	def getEndAt(self):
		return self.EndAt

	def getDescription(self):
		return self.Description

	def setDescription(self, description):
		self.Description = description

	def next(self):
		if not self:
			raise StopIteration
		return self.pop()

	def __str__(self):
		string='"Name":"%s",\n"AlleleNumber":%s,\n"StartAt":%s,\n"EndtAt":%s\n' % (self.Name, self.AlleleNumber, self.StartAt, self.EndAt)
		return str(string)

	def __iter__(self):
		yield self