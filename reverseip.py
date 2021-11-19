from requests import get


def ReverseIP():
    host=input("Enter host >> ")
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print("[+]"+result)
    except:
        print('Invalid IP address')
if __name__=="__main__":
    ReverseIP()