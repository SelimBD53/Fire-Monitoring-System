import requests
from django.conf import settings

def send_sms(phone_number, message):
    
    api_key = settings.BULK_SMS_BD_API_KEY 
    url = "http://bulksmsbd.net/api/smsapi"
    
    payload = {
        'api_key': api_key,
        'type': 'text',
        'number': phone_number,
        'senderid': '8809648903599',
        'message': message,
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  
        print(f"SMS Successfull Send: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"SMS Not Send: {e}")
        return None
