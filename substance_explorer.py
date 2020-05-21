from pypedream import  AlgebraicSystem, Equation, Variable,  Addition, Subtraction, Multiplication, Division, Unit, SI, METRIC,PhysicalDimension, UnitSet, UnitSetDefault, UnitSetSI
from pypedream.thermodynamics import PureComponentFunctionFactory, Substance,ThermodynamicSystem, Properties, PhysicalConstants
from pypedream.database import  purecomponents as pcdb

import math
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px


sys= ThermodynamicSystem("Test")
sys.addComponent(pcdb.Water())
sys.addComponent(pcdb.Isopropanol())
sys.addComponent(pcdb.Methanol())

T= Variable("T", 273.15, SI.K)
T.displayUnit=METRIC.C

c=st.sidebar.selectbox('Substance',sys.components,format_func=str)
p=st.sidebar.selectbox('Property',[e for e in Properties])
fdesc=c.functions[p]
tmin=st.sidebar.slider('Minimum Temperature',-100, 500,25)
tmax=st.sidebar.slider('Maximum Temperature',-100, 500,200)
samples=st.sidebar.number_input('samples',10,150)

TC= c.constants[PhysicalConstants.CriticalTemperature]
PC= c.constants[PhysicalConstants.CriticalPressure]
f=sys.correlationFactory.createFunction(fdesc,T, TC, PC)

def calculate():  
    x=[]
    y=[]
    yd=[]
    for i in range(int(samples)):
        f.reset()
        xi=tmin+(tmax-tmin)/(samples-1)*i
        T.setValue(xi)
        yi= f.eval()
        if(math.isnan(yi)): 
            yi=0
        x.append(xi)
        y.append(yi)
        yd.append(yi)
    df= pd.DataFrame(data={'Temperature':x, 'Property (raw)':y,'Property (display)':yd})
    return df

df=calculate()
st.title('Pure Component Property Visualizer')    
st.write(f"Equation Form: {fdesc.functionType}")
st.write(f"{f}")
fig = px.scatter(df, x =df['Temperature'],y=df['Property (raw)'])
fig.update_xaxes(title="Temperature [°C]")
fig.update_yaxes(title=f"{p.name} [{fdesc.yUnit}]")

st.plotly_chart(figure_or_data=fig)

if st.checkbox("Show raw data"):
    st.write("Raw data")
    st.dataframe(df, width=700, height=300)
#plt.plot(x, y, 'ko') # plotting t, b separately 
#plt.show()