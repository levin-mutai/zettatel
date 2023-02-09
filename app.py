import requests
from messages.resources import send_sms
import json
import os
from dotenv import load_dotenv
load_dotenv()


class API:

    def get_api_key(self):
        url = f"https://portal.zettatel.com/SMSApi/apikey/read?userid={self.userid}&password={self.password}&output={self.output}"

        payload = {}
        headers = {}

        response = requests.request(
            "GET", url, headers=headers, data=payload)

        return response

    def create_api_key(self):
        url = "https://portal.zettatel.com/SMSApi/apikey/create"

        payload = {'userid': self.userid,
                   'password': self.password,
                   'output': self.output}
        files = [

        ]
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)

        return response

    def api_exist(self):
        api = self.get_api_key()

        if api.json()['response']['code'] == "253":
            try:

                res = self.create_api_key()
                if res.json()["response"]["status"] == 'error':
                    raise ValueError(res.json()["response"]["msg"])

                else:
                    res = self.get_api_key()
                    return res.json()['response']['apikeyList']['apikey']

            except Exception as err:
                return str(err)

        else:
            return api.json()['response']['apikeyList']['apikey']


class message:

    # ***********************QUICK SMS*******************************

    def send_quick_SMS(self, to: str, msg: str,):
        """Used to send a quick message to the provided mobile number."""
        try:
            res = send_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, msg, to=to,)
            return res
        except Exception as err:
            return str(err)

    def send_quick_smartlink_sms(self, to: str, msg: str, smartLinkTitle: str):
        """Used to send a message with a link in it. The link will be shortened and assigned the provided smartlink title."""

        try:
            res = send_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, msg, to=to, smartLinkTitle=smartLinkTitle)
            return res
        except Exception as err:
            return str(err)

    def send_quick_sms_Schedule(self, to: str, msg: str, scheduleTime):
        """Sends a scheduled SMS. 'scheduleTime' argument should be passed for it to work"""
        try:
            res = send_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, msg, to=to, scheduleTime=scheduleTime)
            return res
        except Exception as err:
            return str(err)

    # ***********************GROUP SMS*******************************

    def send_group_sms(self, group: str, msg: str):

        try:
            res = send_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, msg, group=group)
            return res
        except Exception as err:
            return str(err)

    def send_group_scheduled_sms(self, group: str, msg: str, scheduleTime):

        try:
            res = send_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, msg, group=group, scheduleTime=scheduleTime)
            return res
        except Exception as err:
            return str(err)

    def send_group_smartlink_sms(self, group: str, msg: str, smartLinkTitle):
        try:
            res = send_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, msg, group=group, smartLinkTitle=smartLinkTitle)
            return res
        except Exception as err:
            return str(err)

    # **********************SMS DELIVERY STATUS****************************


class DeliveryStatus:
    pass
    # TODO: sms delivery status

    # TODO: read senderId

    # TODO: Groups

    # TODO: Contact


class Client(message, API):

    def __init__(self, username, password, senderid, output='json', duplicatecheck='true') -> None:
        self.userid = username
        self.password = password
        self.senderid = senderid
        self.output = output
        self.duplicatecheck = duplicatecheck

    apikey = api_exist()

    print(apikey)
