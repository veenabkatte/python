
class consultant:
    name="";skill="";offer=0.0;exp=0.0
    def __str__(self):
        return self.name+" "+self.skill+"\n"

class org(consultant):
    price=0.0;
    exp=0.0;
    '''def __addMore__(self):
        self.offer+=2.3;
        self.exp+=3'''
    def __add__(self,set):
        self.skill=set;
        
        
        if self.skill == 'java' or self.skill== 'python' and exp>=5 or exp<10:
            self.price=12000
            
        elif self.skill == 'python' or self.skill=='AI'and exp>=3 or exp<8:
            self.price=7000
            
        elif self.skill == 'java' or self.skill=='c++'and exp>=4 or exp<10:
            self.price=5000
            
        else:
            self.price=2.3
    def __str__(self):
         return self.name+" "+" "+self.skill+" "+str(self.exp)+" "+str(self.price)+"\n"

'''com1=org();com1.name="titus";com1+"java";print(com1)
com2=dlithe();com2.name="veena";com2+"javascript";print(com2)'''


com1=org();com1.name="titus";com1+"java";com1+3;print(com1)


'''com1=org();com1.name="titus";com1.exp=5;com1+"java";print(com1)
com2=org();com2.name="veena";com2.exp=8;com2+"AI";print(com2)
com3=org();com3.name="megha";com3.exp=4;com3+"c++";print(com3)
com4=org();com4.name="sharanya";com4.exp=9;com4+"java";print(com4)'''






