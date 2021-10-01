# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import csv
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
data = pd.read_csv("sopnil exel.csv")

Email_id = data['Email Address'].tolist()
Name = data['Name'].tolist()
score = data["Photo"]





for em, nam, pic in zip(Email_id, Name, score):

    fromaddr = "sender email"
    toaddr = em

# instance of MIMEMultipart
    msg = MIMEMultipart()

# storing the senders email address
    msg['From'] = fromaddr

# storing the receivers email address
    msg['To'] = toaddr

# storing the subject
    msg['Subject'] = "Participation Certificate of Ready to Quiz?!"

# string to store the body of the mail
    body = "Dear  " + str(nam) + "\n\n" + "Thank you for participating in Ready to Quiz?! organized by Sopnil Bangladesh. Your presence helped to make this event a great success.\n Here is your participation certificate- "
# attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
    filename = "participation certificate.png"
    attachment = open(pic, "rb")

# instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
    p.set_payload((attachment).read())

# encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
    msg.attach(p)

# creates SMTP session


# start TLS for security

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, 'password')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

