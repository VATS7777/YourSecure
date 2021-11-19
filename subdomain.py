import requests
import json

def fuzz():
    dom=input("Enter Domain >> ")
    url="https://sonar.omnisint.io/subdomains/"+dom
    r=requests.get(url)
    print("Enumerating Subdomains ^-^ .....")
    for i in r.json():
        print("[+]"+i)
    print("Subdomain Enumeration Success")
if __name__=="__main__":
    fuzz()