import streamlit as st
from data.get_data import get_stadistic_team

def search_team():
    st.title('Search by team stadistic')
    st.image('euro2020.jpg')
    stadistic = st.selectbox('Select to view the team with the highest statistics', ['Goals scored', 'Goals received', 'Penalty Goals', 'Possession', 'Shots'])
    if stadistic == 'Goals scored':
        st.image('https://ep01.epimg.net/iconos/v1.x/v1.0/banderas/svg/esp.svg')
        data = get_stadistic_team('goalscored')
        st.write(data['team'],'with' ,data['goals_favor'], 'goals')
    elif stadistic == 'Goals received':
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/800px-Flag_of_Ukraine.svg.png')
        data = get_stadistic_team('goalown')
        st.write(data['team'],'with' ,data['goals_received'], 'goals')
    elif stadistic == 'Penalty Goals':
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/2560px-Flag_of_Italy.svg.png')
        data = get_stadistic_team('penaltys')
        st.write(data['team'],'with' ,data['penaltys_total'], 'penalty goals')
    elif stadistic == 'Possession':
        st.image('https://ep01.epimg.net/iconos/v1.x/v1.0/banderas/svg/esp.svg')
        data = get_stadistic_team('possession')
        st.write(data['team'],'with', data['possession_total'],'%', 'possession')
    elif stadistic == 'Shots':
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/2560px-Flag_of_Italy.svg.png')
        data = get_stadistic_team('shots')
        st.write(data['team'],'with', data['shots'],'shots')