import smtplib
from email.header import Header
from email.mime.text import MIMEText

file_path = "/Users/sihaixianyu/Projects/python/learn-python/basic/email/demo.py"

mail_host = "smtp.qq.com"
mail_user = "sihaixianyu@qq.com"
mail_pass = "kerlpnwzofefdigi"

sender = "sihaixianyu@qq.com"
receivers = ["sihaixianyu@gmail.com"]

with open(file_path) as f:
    msg = MIMEText(f.read(), "plain", "utf-8")

msg["Subject"] = f"The content of {file_path}"
msg["From"] = Header("sihaixianyu@qq.com", "utf-8")
msg["To"] = Header("sihaixianyu@qq.com", "utf-8")

smtp = smtplib.SMTP()
smtp.connect(mail_host, 25)
smtp.login(mail_user, mail_pass)
smtp.sendmail(sender, receivers, msg.as_string())
