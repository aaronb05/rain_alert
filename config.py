import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


def send_sms():
    account_id = os.getenv("account_sid")
    print(account_id)
    token = os.getenv("auth_token")
    client = Client(account_id, token)
    message = client.messages.create(
            body="Rain is in the forecast for today, don't forget your umbrella!",
            from_="+1 830 532 8450",
            to="+1 336 688 4616"
        )

    print(message.sid)

