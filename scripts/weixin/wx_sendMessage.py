#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 微信小工具
from wxpy import *

'''
非图形化界面，例如linux可系统设置参数console_qr=2或True或-2，在命令框生成黑白二维码
Bot(cache_path=True,console_qr=-2)
'''
bot = Bot(cache_path=True,console_qr=-2)
#bot = Bot(cache_path=True)

#发送给自己
bot.self.send("send to myself")

# 搜索好友发消息
friend = bot.friends().search('朗月清风')[0]
friend.send(".....")
