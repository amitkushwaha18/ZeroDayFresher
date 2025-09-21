from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step 2: Twilio credentials (better to load from environment variables)
account_sid = "AC73b7dd747feefefff57362e7f715c1ce"
auth_token = "9312ab9cee4614f5ec5ee60cb41a523c"

client = Client(account_sid, auth_token)

# Step 3: Define function to send WhatsApp message
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",  # Twilio sandbox number
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 4: User input
name = input("Enter the recipient name = ")
recipient_number = input("Enter the recipient WhatsApp number (with country code, e.g. +91XXXXXXXXXX) = ")
message_body = input(f"Enter the message you want to send to {name}: ")

# Step 5: Parse date/time and calculate delay
date_str = input("Enter the date (YYYY-MM-DD): ")
time_str = input("Enter the time (HH:MM in 24-hour format): ")

# Combine date & time into datetime object
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay in seconds
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("❌ The specified time is in the past. Please enter a future date and time.")
else:
    print(f"✅ Message scheduled to be sent to {name} at {schedule_datetime}.")

    # Wait until scheduled time
    time.sleep(delay_seconds)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)
