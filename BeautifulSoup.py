import requests
from bs4 import BeautifulSoup #Kütüphaneleri ekleme

url="http://yaz.tek.firat.edu.tr/tr/duyurular?page=1"
if(url.find("page") != -1):
    i = 1
    while(i<4):
        url = "http://ab.tek.firat.edu.tr/tr/duyurular?page=" + str(i)
        sayfa = requests.get(url)
        icerik = sayfa.content
        soup = BeautifulSoup(icerik, 'html.parser')
        isimlerHepsi = soup.findAll('span', attrs={'class': 'views-field views-field-title'})
        if(sayfa.status_code!=200):
            break
        else:
            j=0
            while(j<len(isimlerHepsi)):
                print("================================"+str(i) +".SAYFA" +str(j+1)+".DUYURU========================")
                print("Duyuru="+isimlerHepsi[j].text.strip())
                j=j+1
            print("=========================")
            print(str(i)+".SAYFANIN SONU")
            print("=========================")
            i=i+1
else:
    sayfa = requests.get(url)
    icerik = sayfa.content
    soup = BeautifulSoup(icerik, 'html.parser')
    isimlerHepsi = soup.findAll('span', attrs={'class': 'views-field views-field-title'})
    j = 0
    while (j < len(isimlerHepsi)):
        print("Duyuru=" + isimlerHepsi[j].text.strip() + "\n")
        j = j + 1