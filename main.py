import argparse
import webcheck

parser = argparse.ArgumentParser(description="NETSAGE cli")
parser.add_argument('--url', '-u', help='Complete url you would like to check')
parser.add_argument('--file', '-f', help='File that contains a list of URLs to check')

args = parser.parse_args()

web_check = webcheck.Webcheck(args.url, args.file)
web_check.read_url()
web_check.web_status()
# print(web_check.urlList)
