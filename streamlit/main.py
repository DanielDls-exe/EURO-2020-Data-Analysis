from nbformat import write
import streamlit as st
from data.get_data import get_all_name_teams, get_team, get_stadistic_team
import pages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
from pages.compare_teams import compare_teams
from pages.compare_players import compare_players
from pages.search_player import search_player
from pages.search_team import search_team

select = st.sidebar.selectbox("Select page", ["Home", "Search Team for stadistic" , "Search Player for stadistic",  "Compare Teams", "Compare Players"])

df = pd.DataFrame()
team_fixed = {}

if select == "Home":
    st.title('Welcome to Euro 2020 Data Analysis')
    st.image('euro2020.jpg')
    name_teams = get_all_name_teams()
    team = st.selectbox('Select a team to view its statistics', name_teams)
    stadistic_team = get_team(team)
    team_fixed['Team'] = stadistic_team['team']
    team_fixed['Possession'] = stadistic_team['possession_total']
    team_fixed['Goals'] = stadistic_team['goals_favor']
    team_fixed['Goals received'] = stadistic_team['goals_received']
    team_fixed['Penalty Goals'] = stadistic_team['penaltys_total']
    team_fixed['Shots'] = stadistic_team['shots']
    df_team = df.append(team_fixed, ignore_index=True)
    df_team.index = ['Team']
    st.dataframe(df_team)
    
if select == "Search Team for stadistic":
    search_team()

if select == "Search Player for stadistic":
    search_player()

if select == "Compare Teams":
    compare_teams()
if select == "Compare Players":
    compare_players()
