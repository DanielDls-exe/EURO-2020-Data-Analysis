from curses import COLOR_BLACK, color_content
import streamlit as st
from data.get_data import get_all_players, get_player, get_all_name_players
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import plotly.express as px
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
load_dotenv()


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

    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, player_one_data, width, label=player1, color = 'Black', edgecolor = 'black')
    rects2 = ax.bar(x + width/2, player_two_data, width, label=player2, color = 'Blue', edgecolor = 'black')

    ax.set_title('Stadistics of Euro 2020')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    st.pyplot(fig)
    pdf = PdfPages('graphic.pdf')
    pdf.savefig(fig)
    pdf.close()
    with open('graphic.pdf', 'rb') as file:
            format = f"{player1}_comparation_{player2}.pdf"
            st.download_button("Download pdf", file , file_name=format)
    correo = st.text_input('Enter your email to receive the data')
    if len(correo) > 0:

        remitente = 'euro2020.data@gmail.com'
        destinatarios = [correo]
        asunto = 'Data comparation'
        cuerpo = 'Here is your data! Have a nice day'
        nombre_adjunto = f"{player1}_comparation_{player2}.pdf"
        password = os.getenv("password")

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open('graphic.pdf', 'rb')
        
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Ciframos la conexión
        sesion_smtp.starttls()

        # Iniciamos sesión en el servidor
        sesion_smtp.login('euro2020.data@gmail.com', password)

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()
