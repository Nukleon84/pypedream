class Unit(object):
    def __init__(self,symbol, name, dimensions):
        self.symbol=symbol
        self.name=name
        self.dimensions=dimensions
        self.factor=1
        self.offset=0

        if(len(dimensions)!=8):
            raise RuntimeError('Argument dimensions must be a list with 8 elements')
  
    def __str__(self):
        return self.symbol

    def __mul__(self, other): 
        newDims=[0,0,0,0,0,0,0,0]          
        for i in range(8):
           newDims[i]= self.dimensions[i]+other.dimensions[i]
        newUnit=  Unit(f"{self.symbol}*{other.symbol}", 'Derived Unit', newDims)
        newUnit.factor=self.factor*other.factor
        newUnit.offset=self.offset+other.offset
        return newUnit
    
    def __truediv__(self, other): 
        newDims=[0,0,0,0,0,0,0,0]          
        for i in range(8):
           newDims[i]= self.dimensions[i]-other.dimensions[i]
        newUnit=  Unit(f"{self.symbol}/{other.symbol}", 'Derived Unit', newDims)
        newUnit.factor=self.factor/other.factor
        newUnit.offset=self.offset-other.offset
        return newUnit

    def __pow__(self, power): 
        newDims=[0,0,0,0,0,0,0,0]          
        for i in range(8):
           newDims[i]= self.dimensions[i]*power
        newUnit=  Unit(f"{self.symbol}^{power}", 'Derived Unit', newDims)
        return newUnit
     
    def printDimensions(self):
        dimSymbols= ["L", "M", "t", "I", "T", "N", "J", "$" ]
        dim=''
        for i in range(8):
            if(self.dimensions[i]!=0):
                if(self.dimensions[i]!=1):
                    dim+=f"{dimSymbols[i]}^{self.dimensions[i]}"
                else:
                    dim+=dimSymbols[i]
                if(i<7):
                    dim+=' '
        return dim.strip()   
    
    def printBaseUnits(self):
        dimSymbols= ["m", "kg", "s", "A", "K", "mol", "cd", "$" ]
        dim=''
        dimdenom=''
        for i in range(8):
            if(self.dimensions[i]>0):
                if(self.dimensions[i]!=1):
                    dim+=f"{dimSymbols[i]}'^'{self.dimensions[i]}"
                else:
                    dim+=dimSymbols[i]
                if(i<7):
                    dim+=' '
            if(self.dimensions[i]<0):
                if(self.dimensions[i]!=-1):
                    dimdenom+=f"{dimSymbols[i]}^{self.dimensions[i]}"
                else:
                    dimdenom+=dimSymbols[i]
                if(i<7):
                    dimdenom+=' '

        
        return dim.strip()+' / '+dimdenom.strip() if dimdenom!='' else dim.strip()                        


#Static Members
    # noinspection PyMethodMayBeStatic
    @staticmethod
    def derive(symbol, name,baseunit, factor=1, offset=0):
        derived=Unit(symbol,name,baseunit.dimensions)        
        derived.factor= baseunit.factor*factor
        derived.offset= baseunit.offset+offset
        return derived
    # noinspection PyMethodMayBeStatic
    @staticmethod
    def getConversionFactor(u1, u2):
        if(u1==None):
            raise RuntimeError("Unit u1 not defined")
        if(u2==None):
            raise RuntimeError("Unit u2 not defined")
        return u1.factor/u2.factor
    # noinspection PyMethodMayBeStatic
    @staticmethod
    def convert(u1, u2, value):     
        if(u1==None):
            raise RuntimeError("Unit u1 not defined")
        if(u2==None):
            raise RuntimeError("Unit u2 not defined")
        baseValue= u1.factor*value+u1.offset
        return (baseValue-u2.offset)/u2.factor