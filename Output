client = Client(account_sid, auth_token)

message = client.messages.create(
    to=output_number, 
    from_=twilio_number,
    body=output_message)

print(message.sid)
