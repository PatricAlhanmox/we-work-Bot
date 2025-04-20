#! -*- coding: utf-8 -*-
"""
Author: ZhenYuSha
Create type_time: 2020-2-24
Info: 定期向企业微信推送消息

Amended by: Ge Zhi
Amend time: 2020-3-22
修订内容: 从原代码每分钟发布一次提醒改成在设定时间点发送提醒，可以实现多时间点发布不同内容提醒信息并@所有人

"""
import requests, json
import datetime
import time

wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ec781bef-a3ad-4553-9142-fe70b0b0565a"    # 测试机器人    将此网址替换成你的群聊机器人Webhook地址
send_message1 = "今天酒测了吗？没酒测的话快去吹一下"
# ============================================= ！！！重置飞一的时间，场次，很重要，计算时间的铆钉点！！！！ ====================================================
Original_Time = datetime.datetime.strptime('2025-04-21', format('%Y-%m-%d'))
Original_Sector = "下午场"


def get_current_time():
    """获取当前时间，当前时分秒"""
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hour = datetime.datetime.now().strftime("%H")
    mm = datetime.datetime.now().strftime("%M")
    ss = datetime.datetime.now().strftime("%S")
    return now_time, hour, mm, ss

# Returns 上午场0/下午场1/休息日2
def MornOrNoon():
    pf = 0
    Res_day = datetime.datetime.today()-Original_Time
    dum = Res_day.days % 12
    if dum >= 6:
        pf = 0
    else:
        pf = 1
    
    rest = Res_day.days % 6
    if rest >= 4:
        pf = 2

    return pf

def sleep_time(hour, m, sec):
    """返回总共秒数"""
    return hour * 3600 + m * 60 + sec


def send_msg(content):
    """@全部，并发送指定信息"""
    data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list":["@all"]}})
    r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
    print(r.json)

def check_time(c_h,c_m):
    second = sleep_time(0, 0, 31)
    Morning = sleep_time(4, 58, 0)
    evening = sleep_time(1, 58, 0)
    match(c_h,c_m):
            case('08','00'):
                print('正在发送提醒')
                send_msg(send_message1)
                time.sleep(Morning)
            case('13','00'):
                print('正在发送提醒')
                send_msg(send_message1)
                return False
            case('14','00'):
                print('正在发送提醒')
                send_msg(send_message1)
                time.sleep(evening)
            case('21','00'):
                print('正在发送提醒')
                send_msg(send_message1)
                return False
            case _:
                print('未到提醒时间')
                time.sleep(second)

def every_time_send_msg(render_f):    #此处定义了每多长时间重复一次此指令，在这里我设置的是每31秒重复一次。且此处设置定时发送消息的时间点（24小时制），在这里我设置的是8点和12点整。
    """每天指定时间发送指定消息"""

    # 设置自动执行间隔时间
    # 循环
    while True:
        # 获取当前时间和当前时分秒
        c_now, c_h, c_m, c_s = get_current_time()
        #print("当前时间：", c_now, c_h, c_m, c_s)
        if render_f == 1:
            print("下午场")
            bool_check = check_time(c_h,c_m)       # 1st remind
            if bool_check == False:
                break
        elif render_f == 0:
            print("上午场")
            bool_check = check_time(c_h,c_m)    # 1st remind
            if bool_check == False:
                break
        else:
            print("休息日")
            send_msg("休息日")
            break

def days():
    return True
        
if __name__ == '__main__':
    today_pf = MornOrNoon()
    if today_pf == 1:
        time.sleep(28500)
    every_time_send_msg(today_pf)