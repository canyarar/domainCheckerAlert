from bs4 import BeautifulSoup
import requests
import time
from termcolor import colored

def is_domain_available(domain):
    try:
        url = "https://www.whois.com/whois/" + domain
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        available = soup.find("td", class_="buylink").text
        if "Before someone else does!" in available:
            return True
        else:
            return False
    except:
        return False

while True:
    domain = "domainname.com"
    if is_domain_available(domain):
        print(colored(domain + " HEMEN ALLL!!!!!", "green"))
    else:
        print(colored(domain + " SATIN ALINAMAZ!", "red"))
    time.sleep(5)
