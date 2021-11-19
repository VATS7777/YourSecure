from socialrecon import reconinput
from webvuln import Webvuln

def Main(a):
    if(a==1):
        reconinput()
    elif(a==2):
        Webvuln()
        

if __name__=="__main__":
    print("""
    

██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗███████╗ ██████╗██╗   ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝███████╗█████╗  ██║     ██║   ██║██████╔╝█████╗  
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝██║  ██║███████║███████╗╚██████╗╚██████╔╝██║  ██║███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                    
""")
   
    print("""
           1.Information Gathering,
           2.Web Vulnerability Scanning,
    """) 
    print("* Please Write 'explore' for Explore Information Gathering Section ")
    print("* Please Write 'showvuln' for Web Vulnerability Scanning Section")
    a=int(input("YourSecure>> "))
    Main(a)
    