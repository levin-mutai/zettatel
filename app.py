import requests
from messages.resources import send_sms
import json
import os
from dotenv import load_dotenv
load_dotenv()


class message:

    # ***********************QUICK SMS*******************************

    def send_quick_SMS(self, to: str, msg: str,):
        """Used to send a quick message to the provided mobile number."""

        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, msg, to=to,)

    def send_quick_smartlink_sms(self, to: str, msg: str, smartLinkTitle: str):
        """Used to send a message with a link in it. The link will be shortened and assigned the provided smartlink title."""

        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, msg, to=to, smartLinkTitle=smartLinkTitle)

    def send_quick_sms_Schedule(self, to: str, msg: str, scheduleTime):
        """Sends a scheduled SMS. 'scheduleTime' argument should be passed for it to work"""

        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, msg, to=to, scheduleTime=scheduleTime)

    # ***********************GROUP SMS*******************************

    def send_group_sms(self, group: str, msg: str):
        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, msg, group=group)

    def send_group_scheduled_sms(self, group: str, msg: str, scheduleTime):
        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, msg, group=group, scheduleTime=scheduleTime)

    def send_group_smartlink_sms(self, group: str, msg: str, smartLinkTitle):
        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, msg, group=group, smartLinkTitle=smartLinkTitle)

    # **********************SMS DELIVERY STATUS****************************


class Client(message):

    def __init__(self, username, password, senderid, output='json', duplicatecheck='true') -> None:
        self.userid = username
        self.password = password
        self.senderid = senderid
        self.output = output
        self.duplicatecheck = duplicatecheck
