import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('fifa.csv')

st.sidebar.header("FIFA")
st.sidebar.image("fifa.jpeg")

c1=st.selectbox("Money related",['Value','Wage','Release Clause'])
st.plotly_chart(px.histogram(df,'Age',c1))

c2=st.selectbox("Value and Wage of players in...",['Nationality','Club'])

cc1,cc2 = st.columns(2)
cc1.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]),x=c2,y='Value'))
cc2.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]),x=c2,y='Wage'))

st.write("Most Skills in each Position")
c3=st.selectbox("Select Position",df['Position'])
dfpos = df[df['Position'] == c3]
max_skill_moves = dfpos[dfpos['Skill Moves'] == dfpos['Skill Moves'].max()]
st.write(max_skill_moves['Name'])

st.write("Most Skills with each Foot")
c4=st.selectbox("Select Foot",df['Preferred Foot'].unique())
dfFoot = df[df['Preferred Foot'] == c4]
max_skill_moves_Foot = dfFoot[dfFoot['Skill Moves'] == dfFoot['Skill Moves'].max()]
st.write(max_skill_moves_Foot['Name'])