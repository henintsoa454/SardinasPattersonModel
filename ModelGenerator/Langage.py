

class Langage:

    def __init__(self):
        self.mots = []

    staticmethod
    def manalaMotVide(L):
        res = []
        for i in range(0,len(L)-1):
            if(L[i]!=''):
                res.append(L[i])      
        return res

    staticmethod
    def getResidus(M , L):
        res = []
    
        for m in M:
            for l in L:
                if(l.startswith(m)):
                    length = len(m)
                    a = l[length::]
                    res.append(a)
        return res

    staticmethod
    def hasVide(L):
        for a in L:
            if a == '':
                return True
        return False
    
    staticmethod
    def checkCode(L):
        
        Lo = L
        L1 = Langage.getResidus(L,L)

        L1 = Langage.manalaMotVide(L1)
        allL = []
        allL.append(Lo)
        allL.append(L1)

        #print(allL)
        i = 2
        b = True
        
        while(b): 
            temp1 = Langage.getResidus(L,allL[i-1])
            temp2 = Langage.getResidus(allL[i-1],L)

            res = False
            temp = temp1+temp2


            if temp in allL or len(allL)>20:
                b = False
                #print("True Periodique")
                res = True
            
            allL.append(temp)

            if(len(temp)==0):
                #print("True vide , longueur :",len(L))
                res = True
                b=False
        

            if(Langage.hasVide(temp1) or Langage.hasVide(temp2)):
                #print("False misy vide , longueur :",len(L))
                res = False 
                b = False
            i+=1
        return res
    

