import requests

def Get2FACode(code):
    url = f"https://2fa.live/tok/{code}"

    payload = {}
    headers = {
    'authority': '2fa.live',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_gcl_au=1.1.594402403.1706617983; _gid=GA1.2.1934874214.1706617983; _gat_gtag_UA_78777107_1=1; _ga_R2SB88WPTD=GS1.1.1706617982.1.1.1706618345.0.0.0; _ga=GA1.2.1777250095.1706617983',
    'if-none-match': 'W/"12-rDHV9VRhFRYjso2EuHBUd/z6Yyc"',
    'referer': 'https://2fa.live/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
