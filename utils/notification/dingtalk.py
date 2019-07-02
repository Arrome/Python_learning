#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

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
    def send_markdown(self, title, text, at_mobiles=[], at_all=False):
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

    '''
        btnOrientation 0-按钮竖直排列，   1-按钮横向排列
        hideAvatar     0-正常发消息者头像，1-隐藏发消息头像
    '''
    def send_action_card(self, is_single=True, **kwargs):
        if is_single:
            self.__send_single_action_card(**kwargs)
        else:
            self.__send_mulit_action_card(**kwargs)

    def __send_single_action_card(self, title, text, single_title, single_url, btn_orientation=False, hide_avatar=False):
        action_card_message = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": title,
                "text": text,
                "singleTitle": single_title,
                "singleURL": single_url,
                "hideAvatar": hide_avatar,
                "btnOrientation": btn_orientation
            }
        }
        self.__post_request(action_card_message)

    def __send_mulit_action_card(self, title, text, btns, btn_orientation=False, hide_avatar=False):
        action_card_message = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": title,
                "text": text,
                "btns": btns,
                "hideAvatar": hide_avatar,
                "btnOrientation": btn_orientation
            }
        }
        self.__post_request(action_card_message)

    # 发送post请求，验证结果
    def __post_request(self, message):
        message = json.dumps(message)
        res = requests.post(self.hook, data=message, headers=self.headers)
        if not res.ok:
            response = json.loads(res.content.decode("utf-8"))
            logging.debug(response["errmsg"])


if __name__ == "__main__":
    ding_talk_robot = DingTalkRobot("xxxxxxxxxxxxxxxxxxxxxxx") #cdf6f6838b6026034d58fc35d987bbd9c80b6e641a05b689d84223e830d62bd0*123
    # ding_talk_robot.send_text("hi")

    # ding_talk_robot.send_link("test", "test", "http://www.baidu.com",
    # # "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=323887866,1970623179&fm=26&gp=0.jpg")

    # ding_talk_robot.send_markdown("test Markdown",
    #                               "#### 测试文本\n![screenshot](https://ss3.bdstatic.com" +
    #                               "/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=323887866,1970623179&fm=26&gp=0.jpg)\n")

    #ding_talk_robot.send_action_card(title="test",text="test",single_title="test",single_url="http://www.baidu.com")

    # btns = [{"title":"test1", "actionURL":"http://www.baidu.com"},{"title":"test2", "actionURL":"http://www.baidu.com"}]
    # ding_talk_robot.send_action_card(is_single=False,title="test", text="test", btns=btns)