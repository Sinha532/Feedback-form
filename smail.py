import smtplib
from email.mime.text import MIMEText


def send_mail(mail):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '2084f20333fb33'
    password = '9a119d2a6a0761'
    message = f"<h3>New Feedback Submission</h3><ul><li>Thanks for the your valuable review.</li></ul>"

    sender_email = 'lokeshsinha746@gmail.com'
    receiver_email = mail
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'amazon Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())