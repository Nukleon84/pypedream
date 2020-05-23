#Hacked Path to find package. Would no be needed when package is installed via pip
import sys
import os
sys.path.append(os.path.abspath('../pypedream'))
from pypedream import MaterialStream, Flowsheet, ThermodynamicSystem
import pypedream.database.purecomponents as pcdb

sys= ThermodynamicSystem("Test")
sys.addComponent(pcdb.Water())
sys.addComponent(pcdb.Isopropanol())
sys.addComponent(pcdb.Methanol())

f= Flowsheet("Test",sys)
S001=f.mstr("S001")

#f.mstr("S001").fvpz(100, 0.5,1000,[ ("Water",0.5), ("Methanol",0.5) ])


print("\Fix Temperature\n\n")
f.mstr("S001").ftpz(100, 82.5,1000,[ ("Water",0.5), ("Methanol",0.5) ])

f.solve()

for v in S001.variables.values():
    print(f"{v.fullName()} = {v.displayValue()} {v.displayUnit}")


print("\Bubble Point\n\n")

f.mstr("S001").fpx(100, 1000,[ ("Water",0.5), ("Methanol",0.5) ])
f.solve()
for v in S001.variables.values():
    print(f"{v.fullName()} = {v.displayValue()} {v.displayUnit}")

print("\nDew Point\n\n")
f.mstr("S001").fpy(100, 1000,[ ("Water",0.5), ("Methanol",0.5) ])
f.solve()
for v in S001.variables.values():
    print(f"{v.fullName()} = {v.displayValue()} {v.displayUnit}")

#print(S001)


'''
f= Flowsheet("Test",sys)
F01= f.unit("F01", "Flash", [f.mstr("S001")],[f.mstr("S002"),f.mstr("S003")])
f.mstr("S001").ftpz(100, 25,1,[ ("Water",0.5), ("Methanol",0.5) ])
f.unit("F01").spec([ ("VF",0.5,SI.none), ("P",1,METRIC.bar) ])
f.init()
f.solve()
print(f.report())
print(f.streamtable())

'''