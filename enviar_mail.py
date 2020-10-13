# -*- coding: utf-8 -*-

import estructura_mail
from Google import Create_Service
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes

mensaje_email = estructura_mail.cuerpo_correo()
destinatario_email = estructura_mail.info_correo()
long_l = len(mensaje_email)

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'gmail',
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

for l in range(long_l):
    emailMsg = mensaje_email[l]
    # create email message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = destinatario_email[l][1]
    mimeMessage['subject'] = 'Revalidación anual clasificación de las bases de datos'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
      
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
     
    message = service.users().messages().send(
        userId='me',
        body={'raw': raw_string}).execute()
 
print(message)
