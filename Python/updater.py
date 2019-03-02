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

host1 = "obliquepeak.com"
user1 = "AhIdNjQmLTDIhBIO"
pass1 = "L5wvZXEbHE6Ji2FU"

host2 = "blog.obliquepeak.com"
user2 = "1QWjUxW1yeFm5qoO"
pass2 = "VECBtCTbsKNQnyaE"

host3 = "demo.obliquepeak.com"
user3 = "WNl8GbiPWQHAK9am"
pass3 = "tO9LE3pmPAuKjrrE"


req1 = requests.post("https://%s:%s@domains.google.com/nic/update?hostname=%s&myip=%s" % (user1, pass1, host1, ipAddr),
                     data={'ssl':'yes', 'protocol':'googledomains', 'login':user1, 'password':pass1})

req2 = requests.post("https://%s:%s@domains.google.com/nic/update?hostname=%s&myip=%s" % (user2, pass2, host2, ipAddr),
                     data={'ssl':'yes', 'protocol':'googledomains', 'login':user2, 'password':pass2})

req3 = requests.post("https://%s:%s@domains.google.com/nic/update?hostname=%s&myip=%s" % (user3, pass3, host3, ipAddr),
                     data={'ssl':'yes', 'protocol':'googledomains', 'login':user3, 'password':pass3})

print(req1.status_code, req1.reason)
print(req2.status_code, req2.reason)
print(req3.status_code, req3.reason)
