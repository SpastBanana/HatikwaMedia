import smtplib, ssl, os
from email.message import EmailMessage
from django.core.mail import send_mail


# # def auth_mail(to, sub, name):
# #     mail_from = "authentication@datalectro.nl"
# #     # mail_pass = os.getenv('auth_mail')
# #     mail_pass = "HdytJ5AYV2"

# #     msg = f"""\
# #     <html>
# #     <head></head>
# #     <body>
# #         <h4>Beste, {name},</h4>
# #         <br>
# #         <p>Bij deze ben je uitgenodigd om deel te nemen aan de website <a href="https://hatikwa-media.nl">Hatikwa Media</a>. Dit is de website waarop alle bladmuziek te vinden is betreffende het koor Hatikwa.</p>
# #         <br>
# #         <p>Voor het instellen van jouw account moet je een wachtwoord aanmaken met de onderstaande link. De gebruikersnaam die je zal gebruiken voor deze website is ten alle tijden hetzelfde als het mailadres waar je deze mail op binnen krijgt.</p>
# #         <br>
# #         <a href="https://hatikwa-media/auth/new-member/register/{name}">Account registreren</a>
# #         <br>
# #         <p>Voor overige vragen, of tech support betreft deze website graag mailen naar één van de onderstaande mail adressen</p>
# #         <p>Bestuur Hatikwa: <a href="mailto:bestuur@hatikwa.nl">bestuur@hatikwa.nl</a></p>
# #         <p>IT en site beheer: <a href="mailto:s.devries@datalectro.nl">s.devries@datalectro.nl</a></p>
# #         <br>
# #         <br>
# #         <h3>Met vriendelijke groet,</h3>
# #         <h4>Bestuur & team IT Hatikwa</h4>
# #     </body>
# #     </html>
# #     """

# #     mail = EmailMessage()
# #     mail["From"] = mail_from
# #     mail["To"] = to
# #     mail["Subject"] = sub
# #     mail.set_content(msg, subtype="html")

# #     with smtplib.SMTP_SSL('smtp.bhosted.nl', port=465, context=ssl.create_default_context()) as server:
# #         server.login(mail_from, mail_pass)
# #         server.sendmail(mail_from, to, mail.as_string())

from django.core.mail import send_mail

def auth_mail(to, sub, name):
    mail_from = "authentication@datalectro.nl"
    mail_pass = "HdytJ5AYV2"

    msg = f"""\
    <html>
    <head></head>
    <body>
        <h4>Beste, {name},</h4>
        <br>
        <p>Bij deze ben je uitgenodigd om deel te nemen aan de website <a href="https://hatikwa-media.nl">Hatikwa Media</a>. Dit is de website waarop alle bladmuziek te vinden is betreffende het koor Hatikwa.</p>
        <br>
        <p>Voor het instellen van jouw account moet je een wachtwoord aanmaken met de onderstaande link. De gebruikersnaam die je zal gebruiken voor deze website is ten alle tijden hetzelfde als het mailadres waar je deze mail op binnen krijgt.</p>
        <br>
        <a href="https://hatikwa-media.nl/auth/new-member/register/{name}">Account registreren</a>
        <br>
        <p>Voor overige vragen, of tech support betreft deze website graag mailen naar één van de onderstaande mail adressen</p>
        <p>Bestuur Hatikwa: <a href="mailto:bestuur@hatikwa.nl">bestuur@hatikwa.nl</a></p>
        <p>IT en site beheer: <a href="mailto:s.devries@datalectro.nl">s.devries@datalectro.nl</a></p>
        <br>
        <br>
        <h3>Met vriendelijke groet,</h3>
        <h4>Bestuur & team IT Hatikwa</h4>
    </body>
    </html>
    """

    send_mail(
        sub,
        None,  # Set the message body to None since it's specified in HTML format
        mail_from,
        [to],
        fail_silently=False,
        html_message=msg,
        auth_user=mail_from,
        auth_password=mail_pass
    )