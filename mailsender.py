import smtplib
myemail="ffhgfghjgv@outlook.com"
connection=smtplib.SMTP("smtp-mail.outlook.com")
connection.starttls()
connection.login(user=myemail,password="sdfghkjhuivv")
connection.sendmail(from_addr=myemail,to_addrs="gggggggggg@gmail.com",msg="Hello")
connection.close()
