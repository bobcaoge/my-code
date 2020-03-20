#coding:utf-8
import smtplib
from log import log
from email.mime.text import MIMEText
def send_email_through_qq(msg_from="378082326@qq.com",auth_passwd='grstceywslrzbihi',msg_to='emailForProgram@163.com',content="", subject="temp",):
    # msg_from="emailForProgram@163.com"
    # passwd='cg378082326'                                      #填入发送方邮箱的授权码
    # msg_to='378082326@qq.com'                                  #收件人邮箱
    # subject = "python邮件测试"
    # content="hello this is a test"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    s = None
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465)#邮件服务器及端口号
        s.login(msg_from, auth_passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        message = "succeeded to send email from {0} to {1}".format(msg_from, msg_to) 
    except Exception:
        message = "failed to send email from {0} to {1}".format(msg_from, msg_to) 
    finally:
        log(message=message)
        if s is not None:
            s.quit()
        else:
            message = "failed to connect the email server" 
        log(message=message)
if __name__ == "__main__":
    send_email_through_qq(content="second test")