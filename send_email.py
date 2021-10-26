from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensagem = "teste de envio de email"

#create message object instance
msg = MIMEMultipart()
msg['From'] = "servicedeskhmg@microcity.com.br"
msg['To'] = "matheus.santana@microcity.com.br"
msg['Subject'] = "TITULO teste 123"
msg.attach(MIMEText(mensagem, 'plain'))

smtp_server = "192.168.0.16"
s = smtplib.SMTP(host=smtp_server, port=25)
s.sendmail(msg['From'], msg['To'], msg.as_string)
s.ehlo_msg
s.helo_resp
s.quit()
print("successfully sent email to %s:" % (msg['To']))