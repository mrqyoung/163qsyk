#!/usr/bin/env python3
#-*-coding:utf-8-*-
#
# Author: Mr.Q.Young, 2013-12-12, v0.1

import urllib.request as ur
import os
import json


url_163 = 'http://c.m.163.com/nc/article/list/T1350383429665/0-20.html'
my_browser = '''"F:\Program Files\Opera x64\opera.exe"'''

def get_list_qsyk(url):
    json_163 = ur.urlopen(url).read()
    '''
    {"T1350383429665":[{"template":"manual","url_3w":"http://help.3g.163.com/13/1201/16/9F17NOK200964JJM.html","timeConsuming":"
    '''
    #print(json_163.decode('utf-8'))
    oJson = json.loads(json_163.decode('utf-8'))
    return oJson['T1350383429665']


def get_urer_url(list_qsyk):
    length = len(list_qsyk)
    for i in range(length):
        print(str(i) + '. ' + list_qsyk[i]['title'])

    print('-' * 32)
    input_ordinal = input(u'\n请输入要看内容的序号：')
    if input_ordinal.isdigit():
        ordinal = int(input_ordinal)
        if 0 <= ordinal < length:
            return list_qsyk[ordinal]['url_3w']
    return list_qsyk[0]['url_3w']


if __name__ == '__main__':
    my_url = get_urer_url(get_list_qsyk(url_163))
    print(my_url)
    os.system(my_browser + ' ' + my_url)

