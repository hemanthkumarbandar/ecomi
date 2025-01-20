import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('hemanthkumarbandaru469@gmail.com','muxf txds hszf tidg')
    msg=EmailMessage()
    msg['FROM']='hemanthkumarbandaru469@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
    