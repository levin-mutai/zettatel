import requests
import re
from utils import is_date


def send_sms(userid, password,  senderid, output, duplicatecheck, to, msg: str, **kwargs):
    extr = kwargs
    url = "https://portal.zettatel.com/SMSApi/send"

    payload = {'userid': userid,
               'password': password,
               'mobile': to,
               'senderid': senderid,
               'msg': msg,
               'sendMethod': 'quick',
               'msgType': 'text',
               'output': output,
               'duplicatecheck': duplicatecheck}

    if kwargs:
        if extr['scheduleTime']:
            if is_date(extr['scheduleTime']):
                payload['scheduleTime'] = extr['scheduleTime']
            else:
                return ValueError("Invalid date and time")
        elif extr['smartLinkTitle']:
            payload['smartLinkTitle'] = extr['smartLinkTitle']

    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    return response


def send_smartlink_sms(userid, password, senderid, output, duplicatecheck, to, msg: str, smartLinkTitle):
    url = "https://portal.zettatel.com/SMSApi/send"

    payload = {'userid': userid,
               'password': password,
               'mobile': to,
               'senderid': senderid,
               'msg': msg,
               'sendMethod': 'quick',
               'msgType': 'text',
               'output': output,
               'duplicatecheck': duplicatecheck,
               'trackLink': 'true',
               'smartLinkTitle': smartLinkTitle
               }
    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    return response


def send_scheduled_sms(userid, password,  senderid, output, duplicatecheck, to, msg: str):
    url = "https://portal.zettatel.com/SMSApi/send"

    payload = {'userid': 'levin',
               'password': 'n1xnS9qM',
               'mobile': '254768850685',
               'senderid': 'ZTSMS',
               'msg': 'This is testing schedule',
               'sendMethod': 'quick',
               'msgType': 'text',
               'scheduleTime': '2019-09-16 13:24',
               'output': 'json',
               'duplicatecheck': 'true'}
    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    print(response.text)
