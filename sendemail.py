def send_email():
    import smtplib
    import getpass
    from email.mime.text import MIMEText

    sender_address = 'waliadhruv100@gmail.com'
    password = getpass.getpass()                                                 #'etoq jokq wlwf akql'
    subject = 'AI Mafia - Machine Learning'
    msg = '''
         Hello Everyone!
         We are pleased to announce that we are going to start a new batch
         of AI Mafia, Hope you will Join!

         Thank you!
         Dhruv Walia
    '''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)

    message = MIMEText(msg)
    message['Subject'] = subject
    message['From'] = sender_address
    message['To'] = 'waliadhruv100@gmail.com'

    server.sendmail(sender_address, 'waliadhruv100@gmail.com', message.as_string())
    server.quit()


# ✅ Call function here, outside
send_email()

#SMTP -> Simple message transfer Protocol as when we want to send messages we have set of rules
#when you want to send email from localhost to other server you have to interact with the inter ferance
# users to get the password from the user and you want to user type the password and its encrypted not encrypted

