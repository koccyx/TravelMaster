import smtplib as sm
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendEmail(message):
    sender = 'royale.nigs@gmail.com'
    password = 'zubdnsudztrlllhe'

    message = MIMEText(message)

    msg = MIMEMultipart()

    try:
        with open('Ticket.pdf', 'rb') as file:
            template = MIMEApplication(file.read(), 'pdf')
    except IOError:
        return 'invalid template'

    msg.attach(message)
    msg.attach(template)

    server = sm.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, f'Subject: Ticket\n{msg.as_string()}')
        return 'YEEE'
    except Exception as _ex:
        return f'{_ex}\n Check your login or password'

if __name__ == '__main__':
    mes = 'HIII'
    print(sendEmail(mes))
