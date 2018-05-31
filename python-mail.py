#!/usr/bin/env python3
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
sender_mail=input("sender mail id: ")
sender_passwd=input("sender password: ")
server.login(sender_mail, sender_passwd)
 
msg = "YOUR MESSAGE!"
server.sendmail(sender_mail, "rsinghal.abc@gmail.com", msg)
server.quit()
