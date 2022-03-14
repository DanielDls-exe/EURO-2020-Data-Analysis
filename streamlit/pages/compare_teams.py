import streamlit as st
from data.get_data import get_all_name_teams, get_team
import pages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, team_one_data, width, label=team1)
    rects2 = ax.bar(x + width/2, team_two_data, width, label=team2)

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
            format = f"{team1}_comparation_{team2}.pdf"
            st.download_button("Download pdf", file , file_name=format)
    correo = st.text_input('Enter your email to receive the data')
    if len(correo) > 0:

        remitente = 'euro2020.data@gmail.com'
        destinatarios = [correo]
        asunto = 'Data comparation'
        cuerpo = 'Here is your data! Have a nice day'
        nombre_adjunto = f"{team1}_comparation_{team2}.pdf"

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
        sesion_smtp.login('euro2020.data@gmail.com','dan121099')

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()
