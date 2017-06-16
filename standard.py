#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import datetime
import json
import os


# 全局定义
class Define:

    group_name = '可说呢！'
    group_nickname = '菜菜酱'
    group_trigger = '菜菜酱菜菜酱'

    help = '''- 菜菜酱还在测试中，可能发生错误或暴走，请多担待\n- 如有问题请 @菜酱 反馈'''

    file_path = '/Users/ICAICS/.qqbot-tmp/plugins/'

    list_astro = ['摩羯座运势', '水瓶座运势', '双鱼座运势', '白羊座运势',
                  '金牛座运势', '双子座运势', '巨蟹座运势', '狮子座运势',
                  '处女座运势', '天秤座运势', '天蝎座运势', '射手座运势']


def onQQMessage(bot, contact, member, content):

    """ QQBot 全局调用入口 """

    # print(bot)
    # print(contact)
    # print(member)
    # print(content)

    # 获取群名称
    group_name = str(contact)
    group_name = group_name[2:-1]
    # print(group_name)

    # 只接收指定群消息
    if contact.ctype == 'group' and group_name == Define.group_name:

        # 获得消息内容
        message = str(content)

        # 只处理触发器开头的消息
        if message.startswith(Define.group_trigger):

            # 去掉触发器
            message = message.replace(Define.group_trigger, '')

            # 去掉 空格 及 @ 符号
            message = message.replace(' ', '')
            message = message.replace('[@ME]', '')

            # 获得处理完成后，等待发送的消息
            result = handle_msg(bot, contact, member, message)

            # 消息非空则回复
            if len(result) > 0:
                bot.SendTo(contact, result)


def handle_msg(bot, contact, member, message):

    """ 处理消息程序 """

    member_name = member.name

    # 处理空消息
    if len(message) == 0:
        return '@' + member_name + ' 需要我为您做什么？\n直接发言「' + Define.group_trigger + ' 你能干什么」查看相关帮助'

    if message == '你能干什么':
        bot.SendTo(contact, Define.help)
        return

    if message in Define.list_astro:
        # 获取指定星座运势
        return get_fate(bot, contact, member_name, message)

    if message.startswith('钦点一人'):
        # 获得钦点的目的用于反馈
        return qindian(bot, contact, member_name, message.replace('钦点一人', ''))

    return '收到消息：' + message


def get_fate(bot, contact, member_name, message):

    # 初始化日期和运势数据文件
    date = str(datetime.date.today())
    filename = os.path.join('.', '.qqbot-tmp', 'plugins', 'today.json')
    fate = load_json(filename)

    # 获取当天运势内容
    fate_today = fate[date]

    # 根据需要的星座返回内容
    if fate_today is not None and len(fate_today) != 0:
        # 获得星座编号
        i = str(Define.list_astro.index(message))
        # 提取对应星座运势
        for astro in fate_today:
            if astro['xingzuo'] == i:
                score = '爱情：' + astro['LoveScore'] + ' 分\n' + \
                        '工作：' + astro['JobScore'] + ' 分\n' + \
                        '财富：' + astro['MoneyScore'] + ' 分\n' + \
                        '健康：' + astro['HealthScore'] + ' 分'
                return '@' + member_name + ' 今天的 ' + message + '：\n' + astro['content'] + '\n' + score

    # 当天运势未更新
    return '@' + member_name + ' 今天的 ' + message + ' 还没有更新'


def qindian(bot, contact, member_name, message):

    # 获得当前群组对象
    group = bot.List('group', Define.group_name)[0]
    # 获得群组内成员
    group_members = bot.List(group)
    # 得到昵称列表
    group_members = [str(m)[3:-1] for m in group_members]

    print(group_members)

    # 尝试 10 次
    you = '[群主]'
    for i in range(10):
        # 随机一人
        you = random.choice(group_members)
        # 是自己
        if you != Define.group_nickname:
            break

    return '@' + member_name + ' 通过 ' + Define.group_nickname + ' 钦点了 @' + you + ' ' + message


def readfile(filename):
    """ 读取文件 """
    filename = '%s%s' % (Define.file_path, filename)
    with open(filename, 'r') as file:
        contents = list()
        while True:
            content = file.readline()
            if content and len(content) > 0 and content != '\n':
                content = content.replace('\n', '')
                contents.append(content)
            else:
                break
        file.close()
        return contents


def load_json(filename):
    """ 读取 JSON 文件 """
    file = open(filename, encoding='utf-8')
    content = json.load(file)
    return content
