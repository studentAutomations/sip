import os
from dhooks import Webhook, Embed, File
import time

# Webhook URL setup
WEBHOOK_URL = [os.getenv('PROBA')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

    # Notify users
    hook.send('**@everyone Nova obavestenja na SIP-u!**')
   
    # File path
    image2_path = 'https://github.com/studentAutomations/sip/blob/main/sip-nova-obavestenja.png' 

    # Send the image
    file = File(image2_path, name='sip-nova-obavestenja.png')
    hook.send(file=file)

    # Send the link
    hook.send('**>>> https://sip.elfak.ni.ac.rs/**')

    # Ensure the file is deleted
    if os.path.exists(image2_path):
        time.sleep(1)  # Ensure file is not locked
        os.remove(image2_path)
        print("Screenshot deleted successfully.")
    else:
        print("Screenshot not found.")
