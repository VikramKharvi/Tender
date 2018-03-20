
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9f7cbd2b9213a9f0ecb5e44b8e015106"
auth_token = "affd536d613697c4c55ab1d9f7e5fedd"
client = Client(account_sid, auth_token)

message = client.messages.create(
    "+919742553048",
    body="Your OTP is 5608",
    from_="+15732790029"
)

print(message.sid)

