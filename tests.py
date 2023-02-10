
import os
from zettatel.message import Client
from dotenv import load_dotenv

load_dotenv()


zettatel = Client(
    os.getenv("username"),
    os.getenv("password"),
    os.getenv("senderId")
)


# zettatel.send_quick_SMS(
#     '254768850685', "this is test from python package")


res = zettatel.get_senderID()
print(res.text)
# zettatel.send_quick_smartlink_sms(
#     '254768850685', 'Get compiled tender edition summary FREE . Register by visiting our website www.makkah.co.ke/tender.php or through our WhatsApp link below. To stop ,dial *456*9*5#', "Samrtlink Title test")
