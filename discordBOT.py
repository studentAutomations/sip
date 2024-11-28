import os
from dhooks import Webhook, Embed, File


WEBHOOK_URL = [os.getenv('PROBA')]


for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone Nova obavestenja na SIP-u!**')
   
    image2_path = 'sip-nova-obavestenja.png' 

    hook.send(file=File(image2_path, name='sip-nova-obavestenja.png'))

    hook.send('**>>> https://sip.elfak.ni.ac.rs/**')
