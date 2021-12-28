#send_email.py# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText


# class SendEmail:
#     global send_user
#     global email_host
#     global password
#     password = "dajiujiu123"#不是邮箱的登录密码，是第三方登录的授权码
#     email_host = "smtp.163.com"
#     send_user = "dajiujiu_123@163.com"
#
#     def send_mail(self, user_list, sub, content):
#         user = "jiujiu"+"<"+send_user+">"#发件人
#         message = MIMEText(content, _subtype='plain', _charset='utf-8')#内容
#         message['Subject'] = sub #主题
#         message['From'] = user #发件人
#         message['To'] = ";".join(user_list)##收件人
#         server = smtplib.SMTP()#创建邮箱服务
#         server.connect(email_host)#连接服务
#         server.login(send_user, password)#登录邮箱
#         server.sendmail(user, user_list, message.as_string())#发送邮件
#         server.close()#关闭邮箱服务
#
#
# if __name__ == '__main__':
#     send = SendEmail()
#     user_list = ['dajiujiu_123@163.com;']
#     sub = "测试邮件"
#     content = "这个是我们的第一封测试邮件"
#     send.send_mail(user_list, sub, content)
#
#
#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# #发送带附件
#
#
# class SendEmail:
#     global send_user
#     global email_host
#     global password
#     password = "dajiujiu123"#不是邮箱的登录密码，是第三方登录的授权码
#     email_host = "smtp.163.com"
#     send_user = "dajiujiu_123@163.com"
#
#     def send_mail(self, user_list, sub, content, attachment):
#         user = "jiujiu"+"<"+send_user+">"#发件人
#         # message = MIMEText(content,_subtype='plain',_charset='utf-8')#实例化一个
#         message = MIMEMultipart()
#         message['Subject'] = sub #主题
#         message['From'] = user #发件人
#         message['To'] = ";".join(user_list)#收件人
#         message.attach(MIMEText(content, 'html', 'utf-8'))
#         att = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf8')
#         att["Content-Type"] = 'application/octet-stream'
#         att["Content-Disposition"] = 'attachment; filename="%s"' % attachment#更改附件名字可以这样写：filename=‘文件命名.后缀’
#         message.attach(att)
#         server = smtplib.SMTP()#创建邮箱服务
#         server.connect(email_host)#连接服务
#         server.login(send_user,password)#登录邮箱
#         server.sendmail(user, user_list, message.as_string())#发送邮件
#         server.close()#关闭邮箱服务
#
#
# if __name__ == '__main__':
#     send = SendEmail()
#     user_list = ['dajiujiu_123@163.com;']
#     sub = "测试邮件"
#     content = "这个是我们的第一封测试邮件"
#     attachment = 'xlrd_test.py'
#     send.send_mail(user_list,sub,content,attachment)




import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#统计结果+报告通知


class SendEmail:
    global send_user
    global email_host
    global password
    password = "dajiujiu123"#不是邮箱的登录密码，是第三方登录的授权码
    email_host = "smtp.163.com"
    send_user = "dajiujiu_123@163.com"

    def send_mail(self, user_list, sub,content, attachment):
        user = "jiujiu"+"<"+send_user+">"#发件人
        # message = MIMEText(content,_subtype='plain',_charset='utf-8')#实例化一个
        message = MIMEMultipart()
        message['Subject'] = sub #主题
        message['From'] = user #发件人
        message['To'] = ";".join(user_list)#收件人
        message.attach(MIMEText(content, 'html', 'utf-8'))
        att = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s"' % attachment
        message.attach(att)
        server = smtplib.SMTP()#创建邮箱服务
        server.connect(email_host)#连接服务
        server.login(send_user,password)#登录邮箱
        server.sendmail(user,user_list,message.as_string())#发送邮件
        server.close()#关闭邮箱服务

        #统计结果，发送邮件
    def sen_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num
        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)

        user_list = ['dajiujiu_123@163.com;']
        sub = "接口自动化测试报告"
        content = "这个是我们的第一封测试邮件"
        attachment = 'xlrd_test.py'
        print('此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s，通过率为%s，失败率为%s')%(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list, sub, content, attachment)


if __name__ == '__main__':
    send = SendEmail()
    send.send_mail([1, 2, 3, 4], [5, 6, 7, 8])

