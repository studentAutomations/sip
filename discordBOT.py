import requests
import os
from dhooks import Webhook

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL)

# Image URL (make sure this is accessible)
image_url = 'https://github.com/studentAutomations/sip/raw/main/sip-nova-obavestenja.png'

# Fetch the image
response = requests.get(image_url)

# Check if the request was successful
if response.status_code == 200:
    # Send the image directly from bytes
    hook.send(file=response.content, filename='image.png')  # Specify a filename for the image

