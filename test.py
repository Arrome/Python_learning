#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


def send(hook, message, headers):
    message = json.dumps(message)
    res = requests.post(hook, message, headers)
    print(res)


class DingTalkRobot(object):
    def __init__(self, access_token):
        self.headers = {"Content-Type": "application/json ;charset=utf-8"}
        self.hook = 'https://oapi.dingtalk.com/robot/send?access_token=' + access_token # 钉钉机器人的webhook地址

    # 文本消息
    def send_text(self, content, at_mobiles=[], at_all=False):
        text_message = {
            "msgtype": "text",
            "text": {"content": content},
            "at": {
                "atMobiles": at_mobiles, # 如果需要@某人，这里写他的手机号 [],
                "isAtAll": at_all  # 如果需要@所有人，这些写1
            }
        }
        #send(self.hook, message=text_message, headers=self.headers)
        message = json.dumps(text_message)
        res = requests.post(self.hook, message, self.headers)
        print(res)

    # 链接消息
    def send_link(self, text, title, link_url, pic_url=""):
        link_message = {
            "msgtype": "link",
            "link": {
                "text": text,
                "title": title,
                "picUrl": pic_url,
                "messageUrl": link_url
            }
        }
        send(self.hook, message=link_message, headers=self.headers)

    # markdown格式消息
    def send_markdown(self,title, text, at_mobiles=[], at_all=False):
        markdown_message = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            },
            "at": {
                "atMobiles": at_mobiles,
                "isAtAll": at_all
            }
        }
        send(self.hook, message=markdown_message, headers=self.headers)

    def send_image(self, pic_url):
        image_message = {
            "msgtype": "image",
            "image": {
                "picURL": pic_url
            }
        }
        send(self.hook, message=image_message, headers=self.headers)


if __name__ == "__main__":
    ding_talk_robot = DingTalkRobot(access_token="cdf6f6838b6026034d58fc35d987bbd9c80b6e641a05b689d84223e830d62bd0")
    ding_talk_robot.send_text("hi啊啊啊")
    #ding_talk_robot.send_image("http://img5.duitang.com/uploads/item/201206/10/20120610123334_t3FzM.thumb.700_0.jpeg")
