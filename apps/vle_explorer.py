import sys
import os
sys.path.append(os.path.abspath('../pypedream'))

from pypedream import  AlgebraicSystem, Equation, Variable,  Addition, Subtraction, Multiplication, Division, Unit, SI, METRIC,PhysicalDimension, UnitSet, UnitSetDefault, UnitSetSI, Flowsheet
from pypedream.thermodynamics import PureComponentFunctionFactory, Substance,ThermodynamicSystem, Properties, PhysicalConstants
from pypedream.database import  purecomponents as pcdb

import math
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

sys= ThermodynamicSystem("Test","NRTL")
sys.addComponent(pcdb.Water())
sys.addComponent(pcdb.Ethanol())
sys.addComponent(pcdb.Methanol())
sys.addComponent(pcdb.Acetone())
sys.addComponent(pcdb.Isopropanol())
sys.fill()

T= Variable("T", 273.15, SI.K)
T.displayUnit=METRIC.C

P= Variable("P", 1e5, SI.Pa)
P.displayUnit=METRIC.mbar

c1=st.sidebar.selectbox('Substance 1',sys.components,format_func=str, index=0)
c2=st.sidebar.selectbox('Substance 2',sys.components,format_func=str,index=1)

tiso=st.sidebar.slider('Isothermal Temperature [°C]',-100, 300,25)
piso=st.sidebar.slider('Isobaric Pressure [mbar]',100, 5000,1013)

steps=st.sidebar.number_input("Number of Samples",10)
calcmode=st.sidebar.radio('Calculation Mode',['Isobaric', 'Isothermal'])

f= Flowsheet("Test",sys)
S001=f.mstr("S001")

def draw_vle(c1,c2, t,p,steps, mode):
    x=[]
    yb=[]
    yd=[]
    for i in range(steps):
        xi= i/(steps-1)
        x.append(xi)
        if(mode=="Isobaric"):
            f.mstr("S001").fpx(1, p,[ (c1.id,xi), (c2.id, 1-xi) ])
            f.solve(silent=True)
            yb.append(f.mstr("S001").getVar("T").displayValue())

        if(mode=="Isothermal"):
            f.mstr("S001").ftx(1, t,[ (c1.id,xi), (c2.id, 1-xi) ])
            f.solve(silent=True)
            yb.append(f.mstr("S001").getVar("P").displayValue())

    for i in range(steps):
        xi= i/(steps-1)        
        if(mode=="Isobaric"):         
            f.mstr("S001").fpy(1, p,[ (c1.id,xi), (c2.id, 1-xi) ])
            f.solve(silent=True)
            yd.append(f.mstr("S001").getVar("T").displayValue())
        if(mode=="Isothermal"):
            f.mstr("S001").fty(1, t,[ (c1.id,xi), (c2.id, 1-xi) ])
            f.solve(silent=True)
            yd.append(f.mstr("S001").getVar("P").displayValue())
  
    df= pd.DataFrame(data={'Composition':x, 'DewCurve':yd,'BubbleCurve':yb})
         
    return df

st.title('VLE Visualizer')     

if(c1!=c2):
    df= draw_vle(c1,c2,tiso, piso, steps,calcmode)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Composition'], y=df['BubbleCurve'],
        name='BubbleCurve',
        mode='lines+markers',
        marker_color='rgba(0, 0, 152, .8)'
    ))

    fig.add_trace(go.Scatter(
        x=df['Composition'], y=df['DewCurve'],
        name='DewCurve',
        mode='lines+markers',
        marker_color='rgba(152, 0, 0, .8)'
    ))

    if(calcmode=="Isobaric"):
        fig.update_yaxes(title="Temperature [°C]")
    else:
        fig.update_yaxes(title="Pressure [mbar]")
    fig.update_xaxes(title=f"Molar fraction of {c1.id}")
    st.plotly_chart(figure_or_data=fig)
    st.write("Raw data")
    st.dataframe(df, width=700, height=300)