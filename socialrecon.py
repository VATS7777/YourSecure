import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from iplocator import iplocate

from webscrap import Links
from NameInfo import Nameinfo
from number import number

def reconinput():
    inp=(input("Info>> "))
    if(inp == '1'):
        recon()
    elif (inp=='2'):
        iplocate()
    elif(inp=='3'):
        Links()
    elif (inp=='4'):
        Nameinfo()
    elif (inp=='5'):
        number()
    elif(inp =='6'):
        urlinfo()
    elif(inp=='7'):
        exit()
    elif(inp=='explore'):
        print("""Select From below Options.
    
            1.Image Footprinting
            2.Trace Single IP
            3.URL lookup in webpages
            4.Information Gathering using Name
            5.Phonenumber verifier
            6.URL redirection checker
            7.Exit
            
            """)
    else:
        print("Enter an valid option")
    while True:
        reconinput()    
        
if __name__=="__main__":
   reconinput()
     
    
