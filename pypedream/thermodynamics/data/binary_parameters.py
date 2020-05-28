import numpy as np
from .enums import BinaryParameterSetType

class BinaryParameterSet(object):
    def __init__(self, name, setType:BinaryParameterSetType, system):
        self.name=name
        self.type=setType
        self.system=system
        self.NC=system.getNumberOfComponents()
 
        self.matrices={}
        self.matrices["A"]=np.zeros((self.NC, self.NC))
        self.matrices["B"]=np.zeros((self.NC, self.NC))
        self.matrices["C"]=np.zeros((self.NC, self.NC))
        self.matrices["D"]=np.zeros((self.NC, self.NC))
        self.matrices["E"]=np.zeros((self.NC, self.NC))
        self.matrices["F"]=np.zeros((self.NC, self.NC))
        return
    
    def getParam(self, matrix, i,j):
        if(i>=0 and j>=0  and i<self.NC and j < self.NC and matrix in self.matrices):
            return self.matrices[matrix][i,j]
        

    def setParam(self, matrix, i,j, value):
        if(i>=0 and j>=0 and i<self.NC and j < self.NC and matrix in self.matrices):
            self.matrices[matrix][i,j]=value
        return

    def setParamSymmetric(self, matrix, i,j, value ):
        if(i>=0 and j>=0 and i<self.NC and j < self.NC  and matrix in self.matrices):
            self.matrices[matrix][i,j]=value
            self.matrices[matrix][j,i]=value
        return 

    def setParamPair(self, matrix, i,j, value, othervalue):
        if(i>=0 and j>=0 and i<self.NC and j < self.NC  and matrix in self.matrices):
            self.matrices[matrix][i,j]=value
            self.matrices[matrix][j,i]=othervalue
        return    