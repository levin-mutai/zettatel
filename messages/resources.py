import requests


def send_sms(userid, password,  senderid, output, duplicatecheck, to, msg: str):
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
