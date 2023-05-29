from datetime import * 
class pacient: 
    dataNaixement:date 
    sexe:str  #H,D 
    estat:str #Lleu,Greu,UCI,mort 
    iniciContagi:date 
    fiContagi:date 
    def __init__(self,Codi:str): 
        self.Codi = Codi 
