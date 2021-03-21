import platform
import random
import time
import webbrowser
from json.decoder import JSONDecodeError

import requests

from config import Configuration


def get_all_centre_vaccinare(judet, persoana):
    headers = {
        'accept': 'application/json',
        'cookie': Configuration.cookie
    }
    body = {
        'countyID': judet,
        'localityID': '',
        'name': '',
        'identificationCode': persoana.cnp,
        'masterPersonnelCategoryID': -4,
        'personnelCategoryID': 32,
        'recipientID': persoana.recipient_id
    }

    ses = requests.Session()
    resp = ses.post(Configuration.search_url, headers=headers, json=body, timeout=120, verify=True)

    try:
        json_response = resp.json()
        # print(json_response['content'])
        return json_response['content']
    except JSONDecodeError as ex:
        print(f'The following error popped up: {ex}')
        print('Maybe check the authentication SESSION cookie?')
        return dict()


def get_viable_centers(vaccin, centre):
    results = filter(lambda c: c['availableSlots'] > 0 and c['boosterID'] == vaccin, centre)
    # print(list(results))
    return list(results)


def open_browser(url):
    if platform.system() == 'Linux':
        chrome_path = '/usr/bin/google-chrome %s'
    elif platform.system() == 'Windows':
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    else:
        print('No habla!')

    webbrowser.get(chrome_path).open(url)


if __name__ == '__main__':
    while True:
        all_centers = get_all_centre_vaccinare(Configuration.looking_for_judet, Configuration.looking_for_person)

        viable_centers = get_viable_centers(Configuration.looking_for_vaccin, all_centers)

        if len(viable_centers) == 0:
            wait = random.randint(20, 60)
            print(f'No results yet! Waiting {wait}s...')
            time.sleep(wait)
        else:
            print(f'Found {len(viable_centers)} results.')
            for res in viable_centers:
                print(
                    f"Disponibil la {res['name']} din {res['countyName']}, localitatea {res['localityName']}, {res['address']}")

            open_browser(Configuration.appointment_url)

            print(f'Waiting {Configuration.time_to_wait_success}s...')
            time.sleep(Configuration.time_to_wait_success)
