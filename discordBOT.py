import os
import requests  # To download the file
from dhooks import Webhook, File
import time

# Webhook URL
WEBHOOK_URL = [os.getenv('PROBA')]

# GitHub raw URL of the file
github_raw_url = "https://raw.githubusercontent.com/studentAutomations/sip/main/sip-nova-obavestenja.png"
local_file_path = "sip-nova-obavestenja.png"

# Download the file locally
response = requests.get(github_raw_url)
if response.status_code == 200:
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print(f"Downloaded file: {local_file_path}")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
    exit(1)

# Send the file using the webhook
for url in WEBHOOK_URL:
    hook = Webhook(url)

    # Notify users
    hook.send("**@everyone Nova obavestenja na SIP-u!**")

    # Send the image
    file = File(local_file_path, name="sip-nova-obavestenja.png")
    hook.send(file=file)

    # Send the link to the website
    hook.send("**>>> https://sip.elfak.ni.ac.rs/**")

# Clean up: Delete the local file
if os.path.exists(local_file_path):
    time.sleep(1)  # Allow time for file handling to finish
    os.remove(local_file_path)
    print(f"Screenshot deleted successfully.")
else:
    print("Screenshot not found.")
