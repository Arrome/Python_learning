#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


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
        self.__post_request(text_message)
        # text_message = json.dumps(text_message)
        # res = requests.post(self.hook, data=text_message, headers=self.headers)
        # print(res)

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
        self.__post_request(link_message)

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
        self.__post_request(markdown_message)

    def send_image(self, pic_url):
        image_message = {
            "msgtype": "image",
            "image": {
                "picURL": pic_url
            }
        }
        self.__post_request(image_message)

    def __post_request(self, message):
        message = json.dumps(message)
        requests.post(self.hook, data=message, headers=self.headers)



if __name__ == "__main__":
    dingTalkRobot = DingTalkRobot("cdf6f6838b6026034d58fc35d987bbd9c80b6e641a05b689d84223e830d62bd0*1")
    dingTalkRobot.send_text("hi")
