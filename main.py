# aadhaar_number = '350277293580'  # Replace with the actual Aadhaar number
# pan = 'CJYPC4916L'  # Replace with the actual PAN

import requests
import json
import argparse

def retrieve_information(aadhaar_number, pan):
    url = 'https://eportal.incometax.gov.in/iec/servicesapi/getEntity'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://eportal.incometax.gov.in',
        'Referer': 'https://eportal.incometax.gov.in/iec/foservices/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sn': 'linkAadhaarPreLoginService'
    }
    payload = {
        'aadhaarNumber': aadhaar_number,
        'pan': pan,
        'preLoginFlag': 'Y',
        'serviceName': 'linkAadhaarPreLoginService'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_data = response.json()
    return response_data.get('messages', [])[0].get('desc')

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pan', help='PAN number')
parser.add_argument('-a', '--aadhaar', help='Aadhaar number')
args = parser.parse_args()

# Check if arguments are provided, otherwise prompt for input
if args.pan and args.aadhaar:
    pan = args.pan
    aadhaar_number = args.aadhaar
else:
    pan = input('Enter PAN number: ')
    aadhaar_number = input('Enter Aadhaar number: ')

result = retrieve_information(aadhaar_number, pan)
print(result)
