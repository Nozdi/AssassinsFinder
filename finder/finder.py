class finder:
	def __init__(self):
		lf.ignore= {'kto', 'Kto'}

	def find(self,zdanie):
        	self.dane=[]
		for s in zdanie.split():
			if s[0].isupper() and s not in self.ignore: self.dane.append(s)
		return self.dane

    
	def checker(self, duze):
		import os	
		print(duze)
		for i in duze:
			os.system("grep "+i+" ../bazy/finbaza.fred | wc -l > tmp.txt")
			f2 = open("tmp.txt")
			tmp=f2.readline()
			if int(tmp)>0:
				print(i,"JEST!")    
		
