import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
df = pd.read_csv('fifa.csv')

# Basic stats
player_count = df['Name'].nunique()
Club_count = df['Club'].nunique()
Nationality_count = df['Nationality'].nunique()

# Sidebar with metrics
st.sidebar.header("FIFA")
st.sidebar.image("fifa.jpeg")
st.sidebar.metric(label="Total Players", value=player_count)
st.sidebar.metric(label="Total Clubs", value=Club_count)
st.sidebar.metric(label="Total Nationalities", value=Nationality_count)

# Tabs for the app
tab1, tab2, tab3, tab_about = st.tabs(['Age', 'Position', 'Money related Analysis', 'About'])

with tab1:
    # Chart for Age analysis
    c1 = st.selectbox("Money related With Age", ['Value', 'Wage', 'Release Clause'])
    st.plotly_chart(px.histogram(df, 'Age', c1))
    st.divider()

    # Club and Nationality Average Age Comparison
    st.write("Average Age of Each Club and Nationality")
    col1, col2 = st.columns(2)
    with col1:
        c5 = st.selectbox("Select Club", df['Club'].unique())
        Cdf = df[df['Club'] == c5]
        team_1_avg_age = Cdf['Age'].mean()
        st.metric(label=f'Average Age of {c5}', value=round(team_1_avg_age, 2))
    with col2:
        c6 = st.selectbox("Nationality", df['Nationality'].unique())
        Ndf = df[df['Nationality'] == c6]
        team_2_avg_age = Ndf['Age'].mean()
        st.metric(label=f'Average Age of {c6}', value=round(team_2_avg_age, 2))
    st.divider()

    # Skill Moves and International Reputation by Age
    st.write("Average Skill Moves and International Reputation by Age")
    df_grouped = df.groupby('Age')[['Skill Moves', 'International Reputation']].mean().reset_index()
    df_melted = df_grouped.melt(id_vars='Age', value_vars=['Skill Moves', 'International Reputation'], var_name='Attribute', value_name='Score')
    st.plotly_chart(px.line(df_melted, x='Age', y='Score', color='Attribute'))
    st.divider()

    # Overall and Potential by Age
    st.write("Average Overall and Potential by Age")
    df_grouped2 = df.groupby('Age')[['Overall', 'Potential']].mean().reset_index()
    df_melted2 = df_grouped2.melt(id_vars='Age', value_vars=['Overall', 'Potential'], var_name='Attribute', value_name='Score')
    st.plotly_chart(px.line(df_melted2, x='Age', y='Score', color='Attribute'))
    st.divider()

with tab2:
    # Analysis based on position
    c3 = st.selectbox("Select Position", df['Position'])
    col3, col4 = st.columns(2)
    with col3:
        st.write("Most Skills in each Position")
        dfpos = df[df['Position'] == c3]
        max_skill_moves = dfpos[dfpos['Skill Moves'] == dfpos['Skill Moves'].max()]
        st.write(max_skill_moves['Name'])

    with col4:
        PreferredFoot = df[df['Position'] == c3]
        st.plotly_chart(px.pie(PreferredFoot, 'Preferred Foot', title=f'Preferred Foot Distribution for {c3}'))
    st.divider()

    # Money-related analysis by position
    c8 = st.selectbox("Select Money related", ['Value', 'Wage', 'Release Clause'])
    st.write(f'Maximum {c8} in Each Position')
    df_grouped3 = df.groupby('Position')[[c8]].max().reset_index()
    st.plotly_chart(px.bar(df_grouped3.drop_duplicates(subset=['Position']), x='Position', y=c8))
    st.divider()

with tab3:
    # Analysis based on nationality or club
    c2 = st.selectbox("Select Club or Nationality.", ['Nationality', 'Club'])
    st.write(f'Value of Each {c2}')
    st.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]), x=c2, y='Value'))
    st.divider()
    st.write(f'Wage of Each {c2}')
    st.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]), x=c2, y='Wage'))
    st.divider()
    st.write(f'Release Clause of Each {c2}')
    st.plotly_chart(px.scatter(df.drop_duplicates(subset=[c2]), x=c2, y='Release Clause'))
    st.divider()

# About Tab
with tab_about:
    st.title("About the Project")
    st.write("""
    ### Project Overview
    This project is a detailed analysis of FIFA data, focusing on various aspects like:
    - Player Ages
    - Skills like 'Skill Moves' and 'International Reputation'
    - Clubs and Nationalities
    - Financial metrics such as 'Value', 'Wage', and 'Release Clause'

    ### Key Features:
    - Age analysis with comparisons between clubs and nationalities.
    - Position-based analysis focusing on skill moves and player attributes.
    - Financial analysis that highlights player value and wages based on different criteria.

    ### Data Source:
    The data used in this project is sourced from FIFA player datasets, which contain detailed information about professional football players from around the world.
    """)

