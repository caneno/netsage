import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress the InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class Webcheck:
    def __init__(self, url, file):
        self.url = url
        self.file = file
        self.urlList = []

    def read_url(self):
        try:
            if self.file is not None:
                with open(self.file, 'r') as file:
                    for line in file:
                        ln = line.strip()
                        self.urlList.append(ln)

        except FileNotFoundError:
            print("File was not found")
        except Exception as e:
            print(e)

    def web_status(self):
        try:
            if self.file:
                for url in self.urlList:
                    resp = requests.get(url, verify=False)
                    print(f"{url}\nStatus Code: {resp.status_code}\nResponse Time: {resp.elapsed}")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
        except requests.exceptions.Timeout as e:
            print(f"Timeout Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An unexpected Request error occurred: {e}")
        except Exception as e:
            print(f"A non-Request related error occurred: {e}")
