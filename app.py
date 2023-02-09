import requests
from messages.resources import send_sms
from API.api import API
from utils import send_request
import json
import os
from dotenv import load_dotenv
load_dotenv()

# TODO: read senderId

# TODO: Groups

# TODO: Contact


class Client:

    def __init__(self, username, password, senderid, output='json', duplicatecheck='true') -> None:
        self.userid = username
        self.password = password
        self.senderid = senderid
        self.output = output
        self.duplicatecheck = duplicatecheck

    def get_api_key(self):

        url = f"https://portal.zettatel.com/SMSApi/apikey/read?userid={self.userid}&password={self.password}&output={self.output}"

        return send_request(url, "GET")

    def create_api_key(self):

        response = send_request(
            "https://portal.zettatel.com/SMSApi/apikey/create",
            "POST",
            {'userid': self.userid, 'password': self.password, 'output': self.output})

        return response

    def api_exist(self):
        global apikey
        api = self.get_api_key()

        if api.json()['response']['code'] == "253":
            try:

                res = self.create_api_key()
                if res.json()["response"]["status"] == 'error':
                    raise ValueError(res.json()["response"]["msg"])

                else:
                    res = self.get_api_key()
                    apikey = res
                    return res.json()['response']['apikeyList']['apikey']

            except Exception as err:
                return str(err)

        else:
            apikey = api
            return api.json()['response']['apikeyList']['apikey']

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

    def delivery_status_by_transactionid(self, transactionid: int):
        url = f"https://portal.zettatel.com/SMSApi/report/status?userid={self.userid}&password={self.password}&apikey= {self.api_exist()}&output={self.output}&uuid={transactionid}"

        return send_request(url, "POST")

    def delivery_status_by_summary(self, groupby='date'):
        url = f"https://portal.zettatel.com/SMSApi/report/smsSummary?userid={self.userid}&password={self.password}&apikey= {self.api_exist()}&groupby={groupby}&output={self.output}"

        return send_request(url, "POST")

    def delivery_status_by_day(self, date):
        url = f"https://portal.zettatel.com/SMSApi/report/day?userid={self.userid}&password={self.password}&apikey= {self.api_exist()}&date={date}&output={self.output}"

        return send_request(url, "POST")

     # **********************Sender ID****************************

    def get_senderID(self):
        return send_request("https://portal.zettatel.com/SMSApi/senderid/read?userid=levin&password=n1xnS9qM&output=json", "GET")
