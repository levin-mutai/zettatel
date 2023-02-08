import requests
from messages.resources import send_sms
import json


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
        # send_smartlink_sms(self.userid, self.password, self.senderid,
        #                    self.output, self.duplicatecheck, to, msg, smartLinkTitle)

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


zettatel = Client("levin", 'n1xnS9qM', 'ZTSM')

zettatel.send_quick_SMS(
    '254768850685', "this is test from python package")
# zettatel.send_quick_smartlink_sms(
#     '254768850685', 'Get compiled tender edition summary FREE . Register by visiting our website www.makkah.co.ke/tender.php or through our WhatsApp link below. To stop ,dial *456*9*5#', "Samrtlink Title test")
