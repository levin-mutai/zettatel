import requests
from messages.resources import send_sms, send_smartlink_sms
import json


class Client:

    def __init__(self, username, password, mobile, senderid, output='json', duplicatecheck='true') -> None:
        self.userid = username
        self.password = password
        self.senderid = senderid
        self.output = output
        self.duplicatecheck = duplicatecheck

    def send_quick_SMS(self, to, msg,):

        send_sms(self.userid, self.password, self.senderid,
                 self.output, self.duplicatecheck, to, msg)

    def send_quick_smartlink_sms(self, to, msg: str, smartLinkTitle):
        send_smartlink_sms(self.userid, self.password, self.senderid,
                           self.output, self.duplicatecheck, to, msg, smartLinkTitle)


zettatel = Client("levin", 'n1xnS9qM',
                  'ZTSM')

# zettatel.send_quick_SMS('254768850685', "this is test from python package")
zettatel.send_quick_smartlink_sms(
    '254768850685', 'Get compiled tender edition summary FREE . Register by visiting our website www.makkah.co.ke/tender.php or through our WhatsApp link below. To stop ,dial *456*9*5#', "Samrtlink Title test")
