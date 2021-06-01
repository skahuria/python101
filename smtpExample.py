import smtplib


smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("FROM EMAIL", 'PASSWORD')
smtpObj.sendmail("FROM EMAIL", "TO EMAIL", 'Subject: SMTP check. \n This is a test email')
smtpObj.quit()