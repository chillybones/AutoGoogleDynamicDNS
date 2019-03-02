import urllib.request
import requests
from bs4 import BeautifulSoup

#Webscrape the IP first and assiging it to ip
IPURL = "http://checkip.dyndns.org"

html = urllib.request.urlopen(IPURL)
soup = BeautifulSoup(html, 'html.parser')
bodyText = soup.find('body')

text = bodyText.text.strip()
splitText = text.split(":")
ipAddr = splitText[1].lstrip()

host1 = "snowsong.org"
user1 = "ET7842U7gXYA7nwU"
pass1 = "0nFxXtbXmfbNCh3g"


req1 = requests.post("https://%s:%s@domains.google.com/nic/update?hostname=%s&myip=%s" % (user1, pass1, host1, ipAddr),
                     data={'ssl':'yes', 'protocol':'googledomains', 'login':user1, 'password':pass1})

print(req1.status_code, req1.reason)