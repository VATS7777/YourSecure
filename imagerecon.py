from halo import Halo
import requests
from bs4 import BeautifulSoup
spinner = Halo(text=' Scanning', spinner='dots')

def recon():
    image=input("Enter the image path >> ")
    try:    
        spinner.start()   
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        url='http://www.google.co.in/searchbyimage/upload'
        secondurl={'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
        response = requests.post(url, files=secondurl,allow_redirects=False)
        fetch=response.headers['Location']
        #print(fetch)
        req=requests.get(fetch,headers=headers)
        socialmedia=["instagram","facebook","twitter","linkedin","github"]
        linklist=[]
        print("[+] Scan started......")
        print("Checking whether the image is associated in any social media ")
        print("Scanning started in Instagram")
        print("Scanning started in Github")
        print("Scanning started in Facebook")
        print("Scanning started in Twitter")
        print("Scanning started in Linkedin")           
        if(req.status_code == 200):
            soup = BeautifulSoup(req.content,'html.parser')
            for g in soup.find_all('div', class_='g'):
                anchors = g.find_all('a')
                if 'href' in str(anchors[0]):
                    linklist.append(anchors[0]['href'])
                    #print(linklist)
            c=0
            for i in socialmedia:
                sm=str(i)
                #print(sm)
                for j in linklist:
                    if sm in str(j):
                        c=c+1   
                        print("[+]"+j)
            if c == 0:
                print("No social Media links associated with this image")             
        spinner.stop()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    recon()
