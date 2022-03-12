import streamlit as st
from data.get_data import get_all_players, get_player, get_all_name_players
import pages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import numpy as np

def compare_players():
    st.title('Compare two players')
    st.image('euro2020.jpg')
    players_to_compare = get_all_name_players()
    player1 = st.selectbox('Select one player to compare', players_to_compare)
    player2 = st.selectbox('Select another player to compare',players_to_compare)

    
    player_one_data = []
    player_two_data = []
    labels = ['Goals Scored', 'Assistance', 'Yellow Cards', 'Red Cards']
    for player_data in get_player(player1):
        if player_data == 'name':
            continue
        player_one_data.append(get_player(player1)[player_data])
    
    for player_data in get_player(player2):
        if player_data == 'name':
            continue
        player_two_data.append(get_player(player2)[player_data])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, player_one_data, width, label=player1)
    rects2 = ax.bar(x + width/2, player_two_data, width, label=player2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title('Stadistics of Euro 2020')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    st.pyplot(fig)
    