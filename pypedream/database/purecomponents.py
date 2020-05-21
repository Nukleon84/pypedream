from .. thermodynamics import Substance
from .. thermodynamics import Properties, FunctionTypes, PhysicalConstants
from .. unitsofmeasure.SI import SI

# Based on Data taken from ChemSep Lite:
# ChemSep v7.41 pure component data - Copyright (c) Harry Kooijman and Ross Taylor (2017) - http://www.perlfoundation.org/artistic_license_2_0 modified  on 11/25/2017 01:11:11 AM by harry
# The properties were converted using an automated routine from the original XML file to a pure Python function

def Water():
        substance = Substance('Water','Water',18.01528 )
        substance.formula='HOH'
        substance.casno='7732-18-5'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 647.14, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 22064000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.344)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 263.15, 647.29, [74.55502, -7295.586, -7.442448, 4.2881E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 273.15, 647.28, [59640000, 0.86515, -1.1134, 0.67764, -0.026925], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Chemsep106, 253.1, 647.29, [32.51621, -3.213004, 7.92411, -7.359898, 2.703522], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 273.1, 533.15, [75539, -22297, 136.02, -0.25622, 0.00018273], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 273.1, 647.13, [-133.7, 6785.7, 18.47, -1.4736E-05, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 273.1, 633.15, [-1.5697, -55.141, 0.7832, 0.0011484, -1.8151E-06], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [33444.62, -5.799206, 0.0251681, -1.43103E-05, 2.76249E-09], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 273.16, 1073.15, [7.002327E-08, 0.934576, 195.6338, -13045.99], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 273.16, 1073.15, [6.5986E-06, 1.3947, 59.478, -15484], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 265.1, 647.1, [-0.031819, 167.09, -3.6781, 0.0053717, -8.4188E-06], SI.K, SI.N/SI.m)
        return substance
def Methanol():
        substance = Substance('Methanol','Methanol',32.04186 )
        substance.formula='CH3OH'
        substance.casno='67-56-1'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 512.64, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 8097000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.565)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 175.47, 512.64, [73.40342, -6548.076, -7.409987, 5.72492E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 175.47, 513.15, [58058000, 0.87168, -0.81501, 0.1695, 0.17846], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 175.47, 503.1, [1.7918, 0.23929, 512.64, 0.21078], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 175.47, 400, [62799, 1254.2, -5.9906, 0.052937, -4.711E-05], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 175.47, 337.85, [-32.996, 1981.4, 3.3666, -3.9246E-06, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 150, 430, [-0.056817, 13.156, -1.2214, -0.00028282, -1.0129E-06], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [39194, -58.085, 0.35012, -0.00036941, 1.2763E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 240, 1000, [3.0654E-07, 0.69658, 204.87, 24.304], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 273, 684.37, [7.8368E-07, 1.7569, 108.12, -21101], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 273.1, 503.15, [-0.094523, 33.559, -2.3648, 0.001011, -2.2169E-06], SI.K, SI.N/SI.m)
        return substance
def Ethanol():
        substance = Substance('Ethanol','Ethanol',46.06844 )
        substance.formula='CH3CH2OH'
        substance.casno='64-17-5'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 513.92, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 6148000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.649)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 159.05, 516.25, [88.0754, -7652.06, -9.471507, 5.928087E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 159.05, 515.65, [63899000, 1.2782, -2.673, 2.7973, -1.0209], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 159, 515.65, [1.3539, 0.24957, 515.66, 0.22099], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 158.5, 399.82, [76684, 675.72, -0.093875, 0.037153, -3.1214E-05], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 200, 440, [8.061, 774.76, -3.0701, -4.3408E-09, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 159.05, 353.15, [0.10247, -120.39, -0.48487, -0.0071706, 3.461E-06], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [36550, 5.2215, 0.46112, -0.00058401, 2.2324E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 200, 1000, [1.2467E-07, 0.7862, 76.034, -2017.3], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 273.15, 1000, [-0.01001, 0.64925, -7360.5, -255250], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 273.15, 503.15, [-0.078773, 19.874, -2.3731, 0.00067227, -2.1132E-06], SI.K, SI.N/SI.m)
        return substance
def Acetone():
        substance = Substance('Acetone','Acetone',58.07914 )
        substance.formula='CH3COCH3'
        substance.casno='67-64-1'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 508.1, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 4700000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.307)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 178.45, 508.2, [72.77713, -5752.936, -7.680083, 6.83076E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 178.45, 508.15, [66943000, 3.4736, -8.9271, 10.062, -4.1656], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 178, 508.2, [1.1051, 0.24556, 508.21, 0.27409], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 178.45, 329.44, [107130, 725.57, 0.95296, 0.025981, -1.439E-05], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 190, 329.44, [-14.064, 1000.7, 0.45349, 3.9456E-07, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 178.45, 343.15, [0.01013, -95.32, -0.21151, -0.0052616, 2.3043E-06], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 200, 1000, [42620, 12.563, 0.4765, -0.00059673, 2.2682E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 178.45, 1000, [3.1012E-08, 0.97616, 23.042, 14.834], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 273.15, 1000, [-26.882, 0.9036, -120950000, -608790000], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 178.45, 490.84, [-0.036769, -1.4835, -2.315, -0.0012473, -1.404E-06], SI.K, SI.N/SI.m)
        return substance
def Isopropanol():
        substance = Substance('Isopropanol','Isopropanol',60.09502 )
        substance.formula='CH3CH(OH)CH3'
        substance.casno='67-63-0'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 508.3, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 4762000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.665)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 185.28, 508.3, [77.70856, -7630.115, -7.63517, 9.965114E-07, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 185.28, 508.3, [110099500, 4.1961, -10.70959, 11.69444, -4.625499], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 185.28, 508.3, [1.1898, 0.26648, 508.3, 0.23986], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 185.26, 480, [-188260, 277.99, 9.4459, 0.010702, -9.1964E-06], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 187.35, 355.41, [-7.4407, 2259.7, -1.1149, 2.963E-07, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 183.65, 410.15, [-0.15761, 49.41, -1.6579, 0.0019566, -3.4939E-06], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [27720, 156.75, 0.30298, -0.00050843, 2.1144E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 185.28, 1000, [1.9931E-07, 0.72329, 178.01, -15.318], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 278.59, 995.41, [0.0028843, 0.91609, 11082, -222500], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 273.15, 355.41, [-0.0068771, -355.64, 0.079386, -0.0097522, 4.9723E-06], SI.K, SI.N/SI.m)
        return substance
def Benzene():
        substance = Substance('Benzene','Benzene',78.11184 )
        substance.formula='-CHCHCHCHCHCH-'
        substance.casno='71-43-2'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 562.05, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 4895000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.209)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 272.04, 562.16, [88.368, -6712.9, -10.022, 7.694E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 273.1, 562.05, [48810000, 0.61066, -0.25882, 0.032238, 0.022475], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 273.1, 562.05, [0.99938, 0.26348, 562.05, 0.27856], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 278.68, 500, [111460, -1854.3, 22.399, -0.028936, 2.8991E-05], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 278.68, 545, [-24.61, 1576.5, 2.1698, -5.1366E-06, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 273.1, 413.1, [0.049539, -177.97, 0.19475, -0.0073805, 2.7938E-06], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [29525, -51.417, 1.1944, -0.0016468, 6.8461E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 273.1, 1000, [3.1366E-08, 0.9675, 8.0285, -35.629], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 250, 1000, [4.9549E-06, 1.4519, 154.14, 26202], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 273.1, 562.05, [-0.02575, -212.19, -0.62089, -0.0059738, 2.1771E-06], SI.K, SI.N/SI.m)
        return substance
def Toluene():
        substance = Substance('Toluene','Toluene',92.13843 )
        substance.formula='(C6H5)CH3'
        substance.casno='108-88-3'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 591.75, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 4108000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.264)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 178.18, 592.15, [32.89891, -5013.81, -1.348918, -1.869928E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 178.18, 569.98, [53752000, 0.50341, 0.24755, -0.72898, 0.37794], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 163.1, 589.8, [0.89799, 0.27359, 591.75, 0.30006], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 178.1, 500, [28291, 48.171, 10.912, 0.0020542, 8.7875E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 178.18, 383.78, [-152.84, 5644.6, 22.826, -4.0987E-05, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 178.18, 474.85, [-0.072922, -23.153, -1.0277, -0.0017074, 3.6787E-07], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 200, 1500, [-43647.49, 603.542, -0.399451, 0.000104382], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 178.18, 1000, [8.5581E-07, 0.49514, 307.82, 1891.6], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 383.78, 1000, [6.541E-06, 1.4227, 190.97, 21890], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 178.18, 569.98, [-0.014261, 19.666, -2.7922, -0.00035188, -3.7637E-06], SI.K, SI.N/SI.m)
        return substance
def P_xylene():
        substance = Substance('P-xylene','P-xylene',106.165 )
        substance.formula='CH3(C6H4)CH3'
        substance.casno='106-42-3'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 616.2, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 3511000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.322)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 282.99, 616.23, [97.352, -8082.1, -11.197, 7.2605E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 286.41, 616.2, [56332000, 0.37965, 0.42395, -0.85683, 0.43704], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 286.41, 616.2, [0.67752, 0.25887, 616.2, 0.27596], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 286.4, 600, [63084, -343.38, 13.438, -0.0033851, 4.5592E-06], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 286.41, 413.1, [-23.916, 1499.8, 2.0719, -3.7065E-06, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 286.41, 413.1, [0.00066881, -122.94, -0.60875, -0.0037322, 9.7446E-07], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [34197, 123.96, 0.98194, -0.0013905, 5.6006E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 273.15, 1273.15, [2.4281E-08, 0.95421, -91.329, 17547], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 320, 1000, [1.261E-07, 1.8916, -453.43, 111720], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 273.1, 616.2, [-0.0080188, 66.097, -3.4878, 0.0018353, -6.8516E-06], SI.K, SI.N/SI.m)
        return substance
def O_xylene():
        substance = Substance('O-xylene','O-xylene',106.165 )
        substance.formula='CH3(C6H4)CH3'
        substance.casno='95-47-6'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 630.3, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 3732000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.312)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 247.98, 630.33, [88.08217, -7844.793, -9.738423, 5.713756E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 247.98, 612, [66979000, 1.259, -1.849, 1.5198, -0.50455], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 247.98, 630.3, [0.69962, 0.26143, 630.3, 0.27365], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 247.8, 473.15, [134490, -170.61, 10.247, 0.0049096, -3.1727E-06], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 247.98, 418.1, [-11.059, 1251.7, -0.076438, 1.254E-06, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 247.98, 417.58, [-0.018751, -22.77, -1.3391, -0.0014281, -6.1692E-07], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [27346, 283.89, 0.41481, -0.00069301, 2.7754E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 247.98, 1273.15, [6.783E-08, 0.82039, -1.2715, 13072], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 320, 1000, [5.9387E-06, 1.356, -206, 65058], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 247.98, 610.18, [-0.011942, 49.212, -3.1236, 0.00059647, -4.5152E-06], SI.K, SI.N/SI.m)
        return substance
def M_xylene():
        substance = Substance('M-xylene','M-xylene',106.165 )
        substance.formula='CH3(C6H4)CH3'
        substance.casno='108-38-3'
        substance.addConstant(PhysicalConstants.CriticalTemperature, 617, SI.K)
        substance.addConstant(PhysicalConstants.CriticalPressure, 3541000, SI.Pa)
        substance.addConstant(PhysicalConstants.AcentricFactor, 0.327)
        substance.addFunction(Properties.VaporPressure, FunctionTypes.Chemsep101, 225.3, 617.05, [97.968, -8164.7, -11.269, 7.2101E-06, 2], SI.K, SI.Pa)
        substance.addFunction(Properties.HeatOfVaporization, FunctionTypes.Chemsep106, 225.3, 617, [59562000, 0.67841, -0.38938, 0.0061115, 0.10219], SI.K, SI.J/SI.kmol)
        substance.addFunction(Properties.LiquidDensity, FunctionTypes.Rackett, 225.3, 617, [0.68902, 0.26086, 617, 0.27479], SI.K, SI.kmol/SI.cum)
        substance.addFunction(Properties.LiquidHeatCapacity, FunctionTypes.Chemsep16, 217, 540.15, [127090, -62.999, 9.3762, 0.0068549, -3.2778E-06], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.LiquidViscosity, FunctionTypes.Chemsep101, 225.3, 413.1, [-13.362, 1141.4, 0.37182, -3.9423E-07, 2], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.LiquidHeatConductivity, FunctionTypes.Chemsep16, 225.3, 413.1, [-0.021158, -27.324, -1.2663, -0.0016664, -3.6744E-07], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.IdealGasHeatCapacity, FunctionTypes.Polynomial, 50, 1000, [33275, 145.81, 0.8805, -0.0012502, 4.9953E-07], SI.K, SI.J/SI.kmol*SI.K)
        substance.addFunction(Properties.VaporViscosity, FunctionTypes.Chemsep102, 225.3, 1273.15, [7.2954E-08, 0.8097, 14.386, 8844.3], SI.K, SI.Pa*SI.s)
        substance.addFunction(Properties.VaporHeatConductivity, FunctionTypes.Chemsep102, 320, 1000, [2.8001E-09, 2.4298, -575.12, 122260], SI.K, SI.W/SI.m/SI.K)
        substance.addFunction(Properties.SurfaceTension, FunctionTypes.Chemsep16, 225.3, 617, [-0.0081275, 86.069, -3.5983, 0.0020602, -6.9588E-06], SI.K, SI.N/SI.m)
        return substance