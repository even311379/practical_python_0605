import smtplib, ssl
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import MyImportantInfo as MIF


def send_mail(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    context = ssl.create_default_context()
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
#     server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls(context=context)
    server.ehlo()
    server.login(send_from,MIF.GMAIL_PASSWORD)
#     server.login(send_from,MIF.HOTMAIL_PASSWORD)
    server.sendmail(send_from, send_to, msg.as_string())
    server.close()

send_mail('even311379@gmail.com',['even311379@hotmail.com'],'你好嗎?','再次測試2',files=[])