import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # 邮件内容设置
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 邮件正文
    msg.attach(MIMEText(message, 'plain'))

    # 发送邮件
    try:
        server = smtplib.SMTP('smtp.qq.com')  # 使用qq邮箱的SMTP服务器，端口号为465，但是不用输端口号
        #server.starttls()  # 开启安全传输层协议（TLS），也不用开启
        server.login(sender_email, sender_password)  # 登录SMTP服务器
        server.send_message(msg)  # 发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败：", str(e))

# 示例用法
sender_email = '1975094751@qq.com'  # 发件人邮箱
sender_password = 'fcnxvwlvkucuceja'  # 发件人邮箱密码
receiver_email = '2665964783@qq.com'  # 收件人邮箱
subject = 'Notice'  # 邮件主题
message = 'Something happened!'  # 邮件内容

send_email(sender_email, sender_password, receiver_email, subject, message)
