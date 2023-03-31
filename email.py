from email.mime.text import MIMEText
from subprocess import Popen, PIPE

msg = MIMEText("Hey Siddharth how are you doing, this is body of the email")
msg["From"] = ""
msg["To"] = ""
msg["Subject"] = "Siddharth!!!This is the subject."
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
