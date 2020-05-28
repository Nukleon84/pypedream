from ..thermodynamics.data.binary_parameters import BinaryParameterSetType
nrtldb=[
        {'CAS1':'7732-18-5','CAS2':'67-56-1','ID1':'Water', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':-95.1322966988728,'BJI':398.954307568438,'CIJ':0.2999,'CJI':0.2999,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'7732-18-5','CAS2':'64-17-5','ID1':'Water', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':-29.1667169887279,'BJI':624.868961352657,'CIJ':0.2937,'CJI':0.2937,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'7732-18-5','CAS2':'67-64-1','ID1':'Water', 'ID2':'Acetone', 'AIJ':0,'AJI':0,'BIJ':666.755585748792,'BJI':409.693790257649,'CIJ':0.5663,'CJI':0.5663,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'7732-18-5','ID1':'Methanol', 'ID2':'Water', 'AIJ':0,'AJI':0,'BIJ':398.954307568438,'BJI':-95.1322966988728,'CIJ':0.2999,'CJI':0.2999,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'64-17-5','ID1':'Methanol', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':-165.055907809984,'BJI':189.345159017713,'CIJ':0.3057,'CJI':0.3057,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'67-64-1','ID1':'Methanol', 'ID2':'Acetone', 'AIJ':0,'AJI':0,'BIJ':92.7265499194847,'BJI':114.008655394525,'CIJ':0.3009,'CJI':0.3009,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'71-43-2','ID1':'Methanol', 'ID2':'Benzene', 'AIJ':0,'AJI':0,'BIJ':363.130837359098,'BJI':582.987671095008,'CIJ':0.4694,'CJI':0.4694,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'108-88-3','ID1':'Methanol', 'ID2':'Toluene', 'AIJ':0,'AJI':0,'BIJ':472.890247584541,'BJI':548.978311191626,'CIJ':0.4643,'CJI':0.4643,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'106-42-3','ID1':'Methanol', 'ID2':'P-xylene', 'AIJ':0,'AJI':0,'BIJ':490.46623389694,'BJI':428.294585346216,'CIJ':0.2921,'CJI':0.2921,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-56-1','CAS2':'108-38-3','ID1':'Methanol', 'ID2':'M-xylene', 'AIJ':0,'AJI':0,'BIJ':498.772594605475,'BJI':413.715630032206,'CIJ':0.291,'CJI':0.291,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'7732-18-5','ID1':'Ethanol', 'ID2':'Water', 'AIJ':0,'AJI':0,'BIJ':624.868961352657,'BJI':-29.1667169887279,'CIJ':0.2937,'CJI':0.2937,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'67-56-1','ID1':'Ethanol', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':189.345159017713,'BJI':-165.055907809984,'CIJ':0.3057,'CJI':0.3057,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'67-64-1','ID1':'Ethanol', 'ID2':'Acetone', 'AIJ':0,'AJI':0,'BIJ':18.2651469404187,'BJI':218.811795491143,'CIJ':0.2987,'CJI':0.2987,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'67-63-0','ID1':'Ethanol', 'ID2':'Isopropanol', 'AIJ':0,'AJI':0,'BIJ':347.292270531401,'BJI':-266.378421900161,'CIJ':0.3125,'CJI':0.3125,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'71-43-2','ID1':'Ethanol', 'ID2':'Benzene', 'AIJ':0,'AJI':0,'BIJ':259.732789855072,'BJI':536.387177938808,'CIJ':0.4774,'CJI':0.4774,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'108-88-3','ID1':'Ethanol', 'ID2':'Toluene', 'AIJ':0,'AJI':0,'BIJ':359.080766908213,'BJI':577.627163848631,'CIJ':0.5292,'CJI':0.5292,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'64-17-5','CAS2':'106-42-3','ID1':'Ethanol', 'ID2':'P-xylene', 'AIJ':0,'AJI':0,'BIJ':386.65625,'BJI':382.487922705314,'CIJ':0.2914,'CJI':0.2914,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-64-1','CAS2':'7732-18-5','ID1':'Acetone', 'ID2':'Water', 'AIJ':0,'AJI':0,'BIJ':409.693790257649,'BJI':666.755585748792,'CIJ':0.5663,'CJI':0.5663,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-64-1','CAS2':'67-56-1','ID1':'Acetone', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':114.008655394525,'BJI':92.7265499194847,'CIJ':0.3009,'CJI':0.3009,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-64-1','CAS2':'64-17-5','ID1':'Acetone', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':218.811795491143,'BJI':18.2651469404187,'CIJ':0.2987,'CJI':0.2987,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-64-1','CAS2':'71-43-2','ID1':'Acetone', 'ID2':'Benzene', 'AIJ':0,'AJI':0,'BIJ':-199.523701690821,'BJI':446.140448872786,'CIJ':0.2971,'CJI':0.2971,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-64-1','CAS2':'108-88-3','ID1':'Acetone', 'ID2':'Toluene', 'AIJ':0,'AJI':0,'BIJ':-124.773148148148,'BJI':366.098128019324,'CIJ':0.295,'CJI':0.295,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'67-63-0','CAS2':'64-17-5','ID1':'Isopropanol', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':-266.378421900161,'BJI':347.292270531401,'CIJ':0.3125,'CJI':0.3125,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'71-43-2','CAS2':'67-56-1','ID1':'Benzene', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':582.987671095008,'BJI':363.130837359098,'CIJ':0.4694,'CJI':0.4694,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'71-43-2','CAS2':'64-17-5','ID1':'Benzene', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':536.387177938808,'BJI':259.732789855072,'CIJ':0.4774,'CJI':0.4774,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'71-43-2','CAS2':'67-64-1','ID1':'Benzene', 'ID2':'Acetone', 'AIJ':0,'AJI':0,'BIJ':446.140448872786,'BJI':-199.523701690821,'CIJ':0.2971,'CJI':0.2971,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'71-43-2','CAS2':'108-88-3','ID1':'Benzene', 'ID2':'Toluene', 'AIJ':0,'AJI':0,'BIJ':30.2928743961353,'BJI':-25.7077797906602,'CIJ':0.3019,'CJI':0.3019,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'71-43-2','CAS2':'106-42-3','ID1':'Benzene', 'ID2':'P-xylene', 'AIJ':0,'AJI':0,'BIJ':-25.2936292270531,'BJI':7.15479066022544,'CIJ':0.3056,'CJI':0.3056,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'71-43-2','CAS2':'108-38-3','ID1':'Benzene', 'ID2':'M-xylene', 'AIJ':0,'AJI':0,'BIJ':-228.556360708535,'BJI':309.621880032206,'CIJ':0.2878,'CJI':0.2878,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-88-3','CAS2':'67-56-1','ID1':'Toluene', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':548.978311191626,'BJI':472.890247584541,'CIJ':0.4643,'CJI':0.4643,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-88-3','CAS2':'64-17-5','ID1':'Toluene', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':577.627163848631,'BJI':359.080766908213,'CIJ':0.5292,'CJI':0.5292,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-88-3','CAS2':'67-64-1','ID1':'Toluene', 'ID2':'Acetone', 'AIJ':0,'AJI':0,'BIJ':366.098128019324,'BJI':-124.773148148148,'CIJ':0.295,'CJI':0.295,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-88-3','CAS2':'71-43-2','ID1':'Toluene', 'ID2':'Benzene', 'AIJ':0,'AJI':0,'BIJ':-25.7077797906602,'BJI':30.2928743961353,'CIJ':0.3019,'CJI':0.3019,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-88-3','CAS2':'106-42-3','ID1':'Toluene', 'ID2':'P-xylene', 'AIJ':0,'AJI':0,'BIJ':113.95944041868,'BJI':-121.651419082126,'CIJ':0.2874,'CJI':0.2874,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'106-42-3','CAS2':'67-56-1','ID1':'P-xylene', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':428.294585346216,'BJI':490.46623389694,'CIJ':0.2921,'CJI':0.2921,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'106-42-3','CAS2':'64-17-5','ID1':'P-xylene', 'ID2':'Ethanol', 'AIJ':0,'AJI':0,'BIJ':382.487922705314,'BJI':386.65625,'CIJ':0.2914,'CJI':0.2914,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'106-42-3','CAS2':'71-43-2','ID1':'P-xylene', 'ID2':'Benzene', 'AIJ':0,'AJI':0,'BIJ':7.15479066022544,'BJI':-25.2936292270531,'CIJ':0.3056,'CJI':0.3056,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'106-42-3','CAS2':'108-88-3','ID1':'P-xylene', 'ID2':'Toluene', 'AIJ':0,'AJI':0,'BIJ':-121.651419082126,'BJI':113.95944041868,'CIJ':0.2874,'CJI':0.2874,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'106-42-3','CAS2':'108-38-3','ID1':'P-xylene', 'ID2':'M-xylene', 'AIJ':0,'AJI':0,'BIJ':141.920692431562,'BJI':-128.288949275362,'CIJ':0.3085,'CJI':0.3085,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-38-3','CAS2':'67-56-1','ID1':'M-xylene', 'ID2':'Methanol', 'AIJ':0,'AJI':0,'BIJ':413.715630032206,'BJI':498.772594605475,'CIJ':0.291,'CJI':0.291,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-38-3','CAS2':'71-43-2','ID1':'M-xylene', 'ID2':'Benzene', 'AIJ':0,'AJI':0,'BIJ':309.621880032206,'BJI':-228.556360708535,'CIJ':0.2878,'CJI':0.2878,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
        {'CAS1':'108-38-3','CAS2':'106-42-3','ID1':'M-xylene', 'ID2':'P-xylene', 'AIJ':0,'AJI':0,'BIJ':-128.288949275362,'BJI':141.920692431562,'CIJ':0.3085,'CJI':0.3085,'DIJ':0,'DJI':0,'EIJ':0,'EJI':0,'FIJ':0,'FJI':0},
]



def fillNRTL(system):
   
    for i, c1 in enumerate(system.components):
        for j, c2 in enumerate(system.components):
            entry = next((e for e in nrtldb if e['CAS1']==c1.casno and e['CAS2']==c2.casno),None)
            if(entry != None):
                #print(f"Found data for {c1.id} and {c2.id}")
                system.binaryParameters[BinaryParameterSetType.NRTL].setParamPair("A", i,j, entry['AIJ'], entry['AJI'])
                system.binaryParameters[BinaryParameterSetType.NRTL].setParamPair("B", i,j, entry['BIJ'], entry['BJI'])
                system.binaryParameters[BinaryParameterSetType.NRTL].setParamPair("C", i,j, entry['CIJ'], entry['CJI'])
                system.binaryParameters[BinaryParameterSetType.NRTL].setParamPair("D", i,j, entry['DIJ'], entry['DJI'])
                system.binaryParameters[BinaryParameterSetType.NRTL].setParamPair("E", i,j, entry['EIJ'], entry['EJI'])
                system.binaryParameters[BinaryParameterSetType.NRTL].setParamPair("F", i,j, entry['FIJ'], entry['FJI'])
    return
