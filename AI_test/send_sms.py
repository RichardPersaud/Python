import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    

    user = "persaudpro2010@gmail.com"
    msg['from'] = user
    password = "vglkxgzqomdtpehn"


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

# email =====
# if __name__ == '__main__':
#     email_alert("hey", "Hello world", "richardpersaud2010@hotmail.com")

# SMS ======
if __name__ == '__main__':
    sub = "Hacking...."
    mg= "...........Hacking"
    email_alert(sub, mg, "16476680831@pcs.rogers.com")
