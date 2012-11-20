class finder:
    def __init__(self):
<<<<<<< HEAD
        lf.ignore= {'kto', 'Kto'}

    def find(self,zdanie):
        self.dane=[]
        for s in zdanie.split():
            if s[0].isupper() and s not in self.ignore: self.dane.append(s)
        return self.dane

=======
        self.dane=[]
        self.ignore={'Kto','kto'}

    def find(self,zdanie):
        for s in zdanie.split():
            if s[0].isupper() and s not in self.ignore: self.dane.append(s)
        return self.dane
    
>>>>>>> ca9b608c76604aa9503b99863ede033db82cd356
    def checker(self, duze):
        import os	
        print(duze)
        for i in duze:
            os.system("grep "+i+" ../bazy/finbaza.fred | wc -l > tmp.txt")
            f2 = open("tmp.txt")
            tmp=f2.readline()
            if int(tmp)>0:
<<<<<<< HEAD
                print(i,"JEST!")		
=======
                print(i,"JEST!")
		
>>>>>>> ca9b608c76604aa9503b99863ede033db82cd356
