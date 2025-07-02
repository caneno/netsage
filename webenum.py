from http.client import responses

import requests
import sys

class PyEnum:
    def __init__(self,url,subdomains):
        self.url = url
        self.subdomains = subdomains


    def enum(self):
        sub_list = open(self.subdomains).read()

        subdoms = sub_list.splitlines()
        for sub in subdoms:
            sub_domains = f"https://{sub}.{self.url}"
            print(sub_domains)
            try:
                resp = requests.get(sub_domains, verify=False)
                print(resp.status_code)

            except requests.ConnectionError:
                pass
            else:
                print("Valid domain:", sub_domains)
