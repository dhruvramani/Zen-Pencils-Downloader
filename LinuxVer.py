import  os
import requests
from bs4 import BeautifulSoup
from urllib.request import Request , urlopen ,urlretrieve

if not os.path.exists("Images"):
    os.makedirs("Images")

def crawl():
    req=requests.get("http://www.zenpencils.com/comic/")
    soup=BeautifulSoup(str(req.text),"html.parser")

    for i in soup.find_all("option"):
        print(i.string)
        getImg(str(i.get("value")),i.string)


def getImg(url,name):
    req=requests.get(url)
    soup=BeautifulSoup(str(req.text),"html.parser")

    fileName=os.path.join("Images",name)

    for i in soup.find_all(id="comic"):
        imgTag=i.contents[1]
        try :
            urlretrieve(str(imgTag.get("src")),fileName+".jpg")
        except :
            print("Error")

crawl()