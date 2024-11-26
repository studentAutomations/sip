import os
from discord import Webhook, RequestsWebhookAdapter, File


WEBHOOK_URL = [os.getenv('proba')]

for url in WEBHOOK_URL:
    hook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())


    def send_message():
    
        message_content = '**@everyone Nova obavestenja na SIP-u!**\n\n**>>> https://sip.elfak.ni.ac.rs/**'
        image_path = 'sip-nova-obavestenja.png'

    
        hook.send(content=message_content)

    
        with open(image_path, 'rb') as image_file:
        hook.send(file=File(image_file, name='sip-nova-obavestenja.png'))


    send_message()



