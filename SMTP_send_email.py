from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
def _format_addr(s):
    name ,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
from_addr = 'czyy1983@163.com'
password = 'yy000000'
to_addr ='diobachio@foxmail.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))


#添加附件
part = MIMEApplication(open('D:/desktop/1.zip','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="1.zip")
msg.attach(part)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()