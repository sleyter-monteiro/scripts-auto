import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

def mail(mail_destinataire, objet, message):
    
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = objet
    multipart_message["From"] = config.adresse_email
    multipart_message["To"] = mail_destinataire
    
    multipart_message.attach(MIMEText(message, "plain"))
    
    serveur_mail = smtplib.SMTP(config.server, config.port)
    serveur_mail.starttls()
    serveur_mail.login(config.adresse_email, config.mot_de_passe)
    serveur_mail.sendmail(config.adresse_email, mail_destinataire, multipart_message.as_string())
    serveur_mail.quit()
    
message_email = """

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""        
mail("sleyter.monteiro@proton.me", "Script Python", message_email)    