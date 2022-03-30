# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "{{your_twilio_sid_here}}"
auth_token = "{{your_twilio_auth_token_here}}"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="This is sent from Umer's python application",
    from_='{{your_twilio_number_here}}',
    to='{{your_number_here}}'
)

print(message.sid)
