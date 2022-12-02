
import qrcode
import base64
import json
import numpy as np
import io
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from google.cloud import storage

def form_trigger(request):
    

    
    payload = request.get_json(silent=True)
    payload = {"responses":['Brayan', 'brayancalderonamorocho@gmail.com', '3002490542', 'Super emocional']}
    print(payload)
    email = payload["responses"][1]
    print(email)
          
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(payload)
    qr.make(fit=True)

    img=qr.make_image(fill='black', back_color="white")
    
    #storage_client = storage.Client()
    #bucket = storage_client.bucket("qr-images-test-endava")
    #blob = bucket.blob("qrcode001.png")
    #blob.upload_from_filename(img)

    message = Mail(
        from_email='brayan.calderon@endava.com',
        to_emails=email,
        subject='Entrada QR',
        html_content=f'<img src="img.jpg" alt="Italian Trulli">')
    

    #encoded_file = base64.b64encode(img).decode()

    #json_data = json.dumps(np.array(img).tolist())

    

    #attachedFile = Attachment(
    #    FileContent(json_data),
    #    FileName('attachment.png'),
    #    FileType('application/pdf'),
    #    Disposition('attachment')
    #)
    #message.attachment = attachedFile
    
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

    
form_trigger(" ")
    
    
    
    
