""" Must have Proton Mail bridge installed first """

import smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEText import MIMEText

port_number =1234
msg = MIMEMultipart()
msg['From'] = 'capts_bot@protonmail.com'
msg['To'] = 'receiver@protonmail.com'
msg['Subject'] = 'PRICE ALERT'
message = 'This is the body of the mail'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('localhost',port_number)
mailserver.login("sender@protonmail.com", "mypassword")
mailserver.sendmail('sender@protonmail.com','receiver@protonmail.com',msg.as_string())
mailserver.quit()