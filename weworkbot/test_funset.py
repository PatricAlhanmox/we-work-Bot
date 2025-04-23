from weworkbot import Bot as wbot
import requests

def send_pic():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ec781bef-a3ad-4553-9142-fe70b0b0565a'
    path = './img.jpg'
    wbot(url)\
        .set_check_counter(1)\
        .set_send_counter(1)\
        .set_image_path(path)\
        .send()
    #wbot(url).set_text("<font color='Green'> 图片发送功能 测试</font>", type='markdown').send()
    print('发送成鲲')
    return
