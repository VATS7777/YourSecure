import requests

def number():
    phonenum = input("Enter Mobile Number with country code >> ")
    url = ("http://apilayer.net/api/validate?access_key=b55f17dc709a489569440211f5f55526&number="+phonenum)
    resp = requests.get(url)
    details = resp.json()
    print('')
    print("Country : "+ details['country_name'])
    print("Location : "+ details['location'])
    print("Carrier : "+ details['carrier'])
    
if __name__=="__main__":
    number()
