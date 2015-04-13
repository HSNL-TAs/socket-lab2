import argparse
import requests

parser = argparse.ArgumentParser(description='PUT command to HTTP Server')
parser.add_argument("-u", "--unix", help="Unix commands", default='ls')
parser.add_argument("-w", "--windows", help="Windows commands", default='dir')
args = parser.parse_args()

win_payload = args.windows
unix_payload = args.unix

r_unix = requests.put("http://140.114.71.175:5000/unix", data=unix_payload)
r_win = requests.put("http://140.114.71.175:5000/win", data=win_payload)


print "Unix page status code:", r_unix.status_code
print "Windows page status code:", r_win.status_code
