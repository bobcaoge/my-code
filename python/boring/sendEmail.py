#coding:utf-8
import smtplib
from log import log
from email.mime.text import MIMEText
def send_email(msg_from="emailForProgram@163.com",auth_passwd='cg378082326',\
                            msg_to='378082326@qq.com',content="", subject="temp",):
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
        if msg_from.endswith("qq.com"):
            s = smtplib.SMTP_SSL("smtp.qq.com",465)#邮件服务器及端口号
        elif msg_from.endswith("163.com"):
            s = smtplib.SMTP("smtp.163.com",25)
        s.login(msg_from, auth_passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        message = "succeeded to send email from {0} to {1}".format(msg_from, msg_to) 
    except Exception as e:
        message = "failed to send email from {0} to {1}".format(msg_from, msg_to) 
        message += " "+str(e)
    finally:
        log(message=message)
        if s is not None:
            s.quit()
        else:
            message = "failed to connect the email server" 
        log(message=message)

if __name__ == "__main__":
    send_email(content="second test")