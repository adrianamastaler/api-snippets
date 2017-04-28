# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Initialize the client
account = "ACCOUNT_SID"
token = "AUTH_TOKEN"
client = Client(account, token)

for c in client.chat.credentials.list():
    print(c.sid)
