from bs4 import BeautifulSoup
import requests
import time
from termcolor import colored

def is_domain_available(domain):
    try:
        url = "https://www.whois.com/whois/" + domain
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        available = soup.find("div", class_="title").text
        if "Looks like this domain has not been registered yet" in available:
            return True
        else:
            return False
    except:
        return False

while True:
    domain = "h3wd.com"
    if is_domain_available(domain):
        print(colored(domain + " HEMEN ALLL!!!!!", "green"))
    else:
        print(colored(domain + " SATIN ALINAMAZ!", "red"))
    time.sleep(5)