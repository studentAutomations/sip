import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL) 

embed = Embed(
    color= 0x499957,
    timestamp='now'
)

hook.send('@everyone Nova obavestenja na SIP-u!')

image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmPtpzziqcXbG795QYLmYvJl6G6CcyKbKHA&s'
image2 = 'https://github.com/studentAutomations/sip/blob/main/sip-nova-obavestenja.png'


embed.add_field(name='Idi na sajt - ', value='https://sip.elfak.ni.ac.rs/')
embed.add_field(name='Vidi obavestenja - ', value=image2)
embed.set_footer(text='Elektronski Fakultet')
embed.set_thumbnail(image1)

hook.send(embed=embed)

embed = {
        "embeds": [{
            "title": "Image Name",
            "description": "Image Description",
            "image": {
                "url": "attachment:https://github.com/studentAutomations/sip/blob/main/sip-nova-obavestenja.png"  # Use the filename here
            }
        }]
    }

    # Prepare the files to be sent
    files = {
        'file': (image_path, open(image_path, 'rb'), 'image/png')  # Adjust MIME type if needed
    }

    # Send the request
    response = requests.post(url, data={'payload_json': json.dumps(embed)}, files=files)
