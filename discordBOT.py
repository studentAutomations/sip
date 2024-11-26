import os
from discord import Webhook, RequestsWebhookAdapter, File


WEBHOOK_URL = [os.getenv('proba')]

for url in WEBHOOK_URL:
    hook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())


    message_content = '**@everyone Nova obavestenja na SIP-u!**\n\n**>>> https://sip.elfak.ni.ac.rs/**'
    image_path = 'sip-nova-obavestenja.png'


    with open(image_path, 'rb') as image_file:
    hook.send(content=message_content, file=File(image_file, name='sip-nova-obavestenja.png'))



