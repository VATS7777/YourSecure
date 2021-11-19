from clickjack import ClickJacking
from hostheader import HostHeader
from subdomain import fuzz
from reverseip import ReverseIP

def Webvuln():
    inp=(input("Vulnerability >> "))
    if(inp == '1'):
        ClickJacking()
    elif(inp=='2'):
        HostHeader()
    elif(inp=='3'):
        fuzz()
    elif(inp=='4'):
        ReverseIP()
    elif(inp=='5'):
        exit()    
    elif(inp=='showvuln'):
        print("""
               1.ClickJacking,
               2.Host header injection.
               3.Subdomain Enumeration.
               4.Reverse IP
               5.Exit
               """)
    else:
        print("Invalid choice")
    while True:
        Webvuln()

if __name__=="__main__":
    Webvuln()