import os
from dhooks import Webhook, Embed, File

# Get the webhook URL from environment variable
WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]

for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        color=0x499957,
        timestamp='now'
    )

    hook.send('@everyone Nova obavestenja na SIP-u!')

    
    image2_path = 'sip-nova-obavestenja.png'  # Local path to the image

    

    # Send the embed and attach the image
    hook.send(file=File(image2_path, name='sip-nova-obavestenja.png'))