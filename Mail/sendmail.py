import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def auth_mail(to, sub, name):
    mail_from = "noreply@hatikwa-media.nl"
    mail_pass = "mknXeC6wu5"

    msg = f"""\
    <html>
    <head></head>
    <body>
        <h4>Beste, {name},</h4>
        <br>
        <p>Bij deze ben je uitgenodigd om deel te nemen aan de website <a href="https://hatikwa-media.nl">Hatikwa Media</a>. Dit is de website waarop alle bladmuziek te vinden is van het koor Hatikwa.</p>
        <p>Voor het instellen van jouw account moet je een wachtwoord aanmaken met de onderstaande link. De gebruikersnaam die je zal gebruiken voor deze website is het mailadres waar je deze mail op binnen hebt gekregen.</p>
        <a href="https://hatikwa-media.nl/auth/new-member/register/{name}">Account registreren</a>
        <br>
        <p>Voor overige vragen of technische ondersteuning voor deze website vraag ik je graag te mailen naar één van de onderstaande mail adressen</p>
        <p>Bestuur Hatikwa: <a href="mailto:bestuur@hatikwa.nl">bestuur@hatikwa.nl</a></p>
        <p>IT en site beheer: <a href="mailto:sebastiaan@huizedevries.nl">sebastiaan@huizedevries.nl</a></p>
        <br>
        <br>
        <h4>Met vriendelijke groet,</h4>
        <h5>Sebastiaan de Vries | IT Hatikwa</h5>
    </body>
    </html>
    """

    # Create a MIMEText object to hold the HTML content
    html_content = MIMEText(msg, "html")

    # Create a MIMEMultipart object to hold the email content
    email = MIMEMultipart()
    email.attach(html_content)

    email["Subject"] = sub
    email["From"] = mail_from
    email["To"] = to

    # Create an SMTP connection
    smtp = smtplib.SMTP_SSL("smtp.bhosted.nl", 465)  # Replace with your SMTP server and port
    smtp.login(mail_from, mail_pass)

    # Send the email
    smtp.send_message(email)

    # Close the SMTP connection
    smtp.quit()


def reset_email(to, sub, name):
    mail_from = "noreply@hatikwa-media.nl"
    mail_pass = "mknXeC6wu5"

    msg = f"""\
    <html>
    <head></head>
    <body>
        <h4>Beste, {name},</h4>
        <br>
        <p>Jouw account & wachtwoord voor <a href="https://hatikwa-media.nl">Hatikwa Media</a> zijn gereset.</p>
        <p>Je kunt met de onderstaande link je account en wachtwoord opnieuw instellen. Dit werkt hetzelfde als toen je voor het eerst een account aanmaakte op deze site.</p>
        <a href="https://hatikwa-media.nl/auth/new-member/register/{name}">Account registreren</a>
        <br>
        <p>Voor overige vragen of technische ondersteuning voor deze website vraag ik je graag te mailen naar één van de onderstaande mail adressen</p>
        <p>Bestuur Hatikwa: <a href="mailto:bestuur@hatikwa.nl">bestuur@hatikwa.nl</a></p>
        <p>IT en site beheer: <a href="mailto:sebastiaan@huizedevries.nl">sebastiaan@huizedevries.nl</a></p>
        <br>
        <br>
        <h4>Met vriendelijke groet,</h4>
        <h5>Sebastiaan de Vries | IT Hatikwa</h5>
    </body>
    </html>
    """

    # Create a MIMEText object to hold the HTML content
    html_content = MIMEText(msg, "html")

    # Create a MIMEMultipart object to hold the email content
    email = MIMEMultipart()
    email.attach(html_content)

    email["Subject"] = sub
    email["From"] = mail_from
    email["To"] = to

    # Create an SMTP connection
    smtp = smtplib.SMTP_SSL("smtp.bhosted.nl", 465)  # Replace with your SMTP server and port
    smtp.login(mail_from, mail_pass)

    # Send the email
    smtp.send_message(email)

    # Close the SMTP connection
    smtp.quit()