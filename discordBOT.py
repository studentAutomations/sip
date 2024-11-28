import os
from dhooks import Webhook, Embed, File
import time

WEBHOOK_URL = [os.getenv('PROBA')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone Nova obavestenja na SIP-u!**')
   
    image2_path = 'sip-nova-obavestenja.png' 

    # Send the image
    with File(image2_path, name='sip-nova-obavestenja.png') as file:
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
