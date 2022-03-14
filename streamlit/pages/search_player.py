import streamlit as st
from data.get_data import get_stadistic_player, get_stadistic_player_cards


def search_player():
    st.title('Search by player stadistic')
    st.image('euro2020.jpg')
    stadistic = st.selectbox('Select to view the player with the highest statistics', ['Goals', 'Assistance', 'Penalty Goals', 'Yellow cards', 'Red cards'])
    if stadistic == 'Goals':
        st.image('https://as01.epimg.net/futbol/imagenes/2021/07/11/eurocopa/1626020001_645226_1626041642_noticia_normal_recorte1.jpg')
        data = get_stadistic_player('goals')
        st.write(data['name'],'with' ,data['goals'], 'goals')
    elif stadistic == 'Assistance':
        st.image('https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/06/17/21/zuber-goal.jpg?width=1200')
        data = get_stadistic_player('assist')
        st.write(data['name'],'with' ,data['assistance'], 'assistance')
    elif stadistic == 'Yellow cards':
        st.image('https://phantom-marca.unidadeditorial.es/476d7956be5a9e8add3438a154d4326e/resize/1320/f/jpg/assets/multimedia/imagenes/2021/07/05/16254987365421.jpg')
        data = get_stadistic_player_cards('yellow')
        st.write(data['name'],'with' ,data['yellow_cards'], 'yellow cards')
    elif stadistic == 'Red cards':
        st.image('https://images.news18.com/ibnlive/uploads/2021/06/1623858583_sports-2021-06-16t211526.177.png')
        data = get_stadistic_player_cards('red')
        st.write(data['name'],'with' ,data['red_cards'], 'red cards')
    