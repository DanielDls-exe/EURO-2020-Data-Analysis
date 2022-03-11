import streamlit as st
from data.get_data import get_all_name_teams

select = st.sidebar.selectbox("Select page", ["Home", "Compare Teams", "Compare Players"])

if select == 'Home':
    st.title('Welcome to Euro 2020 Data Analysis')
    st.image('euro2020.jpg')
    a = get_all_name_teams()
    st.selectbox('Select a team to view its statistics', a)
elif select == 'Compare Teams':
    st.text('Compare teams')    
elif select == 'Compare Players':
    st.text('Compare players')  