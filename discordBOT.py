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

 hook.send(file=response.content)

