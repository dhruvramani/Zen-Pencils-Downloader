import  os
from bs4 import BeautifulSoup
from urllib.request import Request , urlopen ,urlretrieve

if not os.path.exists("Images"):
    os.makedirs("Images")

hdr={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def crawl():
    req=Request("http://www.zenpencils.com/comic/",headers=hdr)
    soup=BeautifulSoup(str(urlopen(req).read()),"html.parser")

    for i in soup.find_all("option"):
        print(i.string)
        getImg(str(i.get("value")),i.string)


def getImg(url,name):
    req=Request(url,headers=hdr)
    soup=BeautifulSoup(str(urlopen(req).read()),"html.parser")

    fileName=os.path.join("Images",name)

    for i in soup.find_all(id="comic"):
        imgTag=i.contents[1]
        try :
            urlretrieve(str(imgTag.get("src")),fileName+".jpg")
        except :
            print("Error")

crawl()