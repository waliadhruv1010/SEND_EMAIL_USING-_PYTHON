def send_email():
    import smtplib
    import getpass
    from email.mime.text import MIMEText

    sender_address = 'Sender Email'
    password = getpass.getpass()                                             
    subject = 'Machine Learning'
    msg = '''
         Hello Everyone!
         We are currently onLinkdien ,If we doing good then we will make 
         You tube Channel.Lets see !

         Thank you!
         Dhruv Walia
    '''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)

    message = MIMEText(msg)
    message['Subject'] = subject
    message['From'] = sender_address
    message['To'] = 'Email'

    server.sendmail(sender_address, 'Email', message.as_string())
    server.quit()


# ✅ Call function here, outside
send_email()

#SMTP -> Simple message transfer Protocol as when we want to send messages we have set of rules
#when you want to send email from localhost to other server you have to interact with the inter ferance
# users to get the password from the user and you want to user type the password and its encrypted not encrypted

