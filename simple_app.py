
import streamlit as st
import plotly.express as px
import seaborn as sns
import numpy as np

#loading datasets

tita = sns.load_dataset('titanic')

#plots
px.bar(tita,x="sex",y="alive")

#stremlit
st.title("data visualisation  with plotly")

#section 1
st.header("plot 1-titanic")
st.plotly_chart(fig)
st.markdown('''**insight observed**:(there r more female survivours)''')

