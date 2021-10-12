# libreris
import smtplib , ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# email
sender = '#sender email#'
receiver = '#receiver email#'
body = '#msg#'

#msg
msg = MIMEText(body ,'html')
msg['Subject'] ='#the  email Subject#'
msg['From'] = '#sendr#'
msg['To'] = ','.join(receiver)

#login
s=smtplib.SMTP_SSL(host= '#sender emil#' , port= 465)
s.login(user='#sender email#' , password= '# email password#')
s.sendmail(sender,receiver,msg.as_string())
s.quit()



from tkinter import *
from tkinter import messagebox


def hello():
  
   messagebox.showinfo("Erorre","your computer is no compatibel")

hello()
