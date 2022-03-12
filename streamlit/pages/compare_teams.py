import streamlit as st
from data.get_data import get_all_name_teams, get_team
import pages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import numpy as np

def compare_teams():
    st.title('Compare two teams')
    st.image('euro2020.jpg')
    teams_to_compare = get_all_name_teams()
    team1 = st.selectbox('Select one team to compare', teams_to_compare)
    team2 = st.selectbox('Select another team to compare',teams_to_compare)

    
    team_one_data = []
    team_two_data = []
    labels = ['Possession', 'Goals Scored', 'Goals Received', 'Penaltys', 'Shots']
    for team_data in get_team(team1):
        if team_data == 'team':
            continue
        team_one_data.append(get_team(team1)[team_data])
    
    for team_data in get_team(team2):
        if team_data == 'team':
            continue
        team_two_data.append(get_team(team2)[team_data])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, team_one_data, width, label=team1)
    rects2 = ax.bar(x + width/2, team_two_data, width, label=team2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title('Stadistics of Euro 2020')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    st.pyplot(fig)