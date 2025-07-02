import requests
import argparse

class Webcheck:
    def __init__(self,url,file):
        self.url = url
        self.file = file
        self.urlList = []

    def read_url(self):
        try:
            if self.file is not None:
                with open(self.file, 'r') as file:
                    for line in file:
                        l = line.strip()
                        self.urlList.append(l)

        except FileNotFoundError:
            print("File was not found")
        except Exception as e:
            print(e)