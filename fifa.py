import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('fifa.csv')

player_count = df['Name'].nunique()
Club_count = df['Club'].nunique()
Nationality_count = df['Nationality'].nunique()


st.sidebar.header("FIFA")
st.sidebar.image("fifa.jpeg")
st.sidebar.metric(label="Total Players", value=player_count)
st.sidebar.metric(label="Total Clubs", value=Club_count)
st.sidebar.metric(label="Total Nationalities", value=Nationality_count)


tab1,tab2,tab3=st.tabs(['Age','Position','Money related Analysis'])

with tab1:
    c1=st.selectbox("Money related",['Value','Wage','Release Clause'])
    st.plotly_chart(px.histogram(df,'Age',c1))
    st.divider()

    st.write("Average Age of Each Club and Nationality")
    col1, col2 = st.columns(2)
    with col1:
        c5=st.selectbox("Select Club",df['Club'].unique())
        Cdf=df[df['Club'] == c5]
        team_1_avg_age = Cdf['Age'].mean()
        st.metric(label=f'Average Age of {c5}', value=round(team_1_avg_age, 2))
    with col2:
        c6=st.selectbox("Nationality",df['Nationality'].unique())
        Ndf=df[df['Nationality'] == c6]
        team_2_avg_age = Ndf['Age'].mean()
        st.metric(label=f'Average Age of {c6}', value=round(team_2_avg_age, 2))
    st.divider()

    st.write("Average Skill Moves and International Reputation by Age")
    df_grouped = df.groupby('Age')[['Skill Moves', 'International Reputation']].mean().reset_index()
    df_melted = df_grouped.melt(id_vars='Age', value_vars=['Skill Moves', 'International Reputation'],var_name='Attribute', value_name='Score')
    st.plotly_chart(px.line(df_melted, x='Age',y='Score', color='Attribute'))
    st.divider()

    st.write("Average Overall and Potential by Age")
    df_grouped2 = df.groupby('Age')[['Overall', 'Potential']].mean().reset_index()
    df_melted2 = df_grouped2.melt(id_vars='Age', value_vars=['Overall', 'Potential'],var_name='Attribute', value_name='Score')
    st.plotly_chart(px.line(df_melted2, x='Age',y='Score', color='Attribute'))
    st.divider()

with tab2:
    
    c3=st.selectbox("Select Position",df['Position'])
    col3,col4=st.columns(2)
    with col3:
        st.write("Most Skills in each Position")
        
        dfpos = df[df['Position'] == c3]
        max_skill_moves = dfpos[dfpos['Skill Moves'] == dfpos['Skill Moves'].max()]
        st.write(max_skill_moves['Name'])
        

    with col4:
        PreferredFoot=df[df['Position'] == c3]
        st.plotly_chart(px.pie(PreferredFoot,'Preferred Foot', title=f'Preferred Foot Distribution for {c3}'))
    st.divider()


    c8=st.selectbox("Select Money related",['Value','Wage','Release Clause'])
    st.write(f'Maximum {c8} in Each Position')
    df_grouped3 = df.groupby('Position')[[c8]].max().reset_index()
    st.plotly_chart(px.bar(df_grouped3.drop_duplicates(subset=['Position']),x='Position',y=c8))
    st.divider()

with tab3:
    c2=st.selectbox("Value and Wage of players in...",['Nationality','Club'])

    st.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]),x=c2,y='Value'))
    st.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]),x=c2,y='Wage'))
    st.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]),x=c2,y='Release Clause'))
    st.divider()
