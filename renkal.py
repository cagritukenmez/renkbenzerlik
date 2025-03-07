import requests
from bs4 import BeautifulSoup
import sys
import time
from renkbenzerlik import arrange,vectorSimilarity

def convertHexToDecimal(hex):
  rgbList = []
  rgbList.append(int(hex[0:2],16))
  rgbList.append(int(hex[2:4],16))
  rgbList.append(int(hex[4:6],16))
  return rgbList

def enYakinBenzerlikOraniBul(input_rgb,renkListesi):
  enbuyuk = 0
  enbuyukIndex = 0
  indeks = 0
  input_normalize = arrange(input_rgb,3,0,255)
  for renk in renkListesi:
    benzerlik_oran = vectorSimilarity(input_normalize,arrange(renk[1],3,0,255))
    if benzerlik_oran > enbuyuk:
      enbuyuk = benzerlik_oran
      enbuyukIndex = indeks
    print(benzerlik_oran)
    
    
    return renkListesi[enbuyukIndex][0]+str(benzerlik_oran)

counter =0
linkListesi=[]
#encoding
sys.stdout.reconfigure(encoding='utf-8')
r = requests.get("https://www.colorhexa.com/color-names")
#wait for page to load
time.sleep(4)
soup = BeautifulSoup(r.content, "lxml")
ürünler = soup.find_all("table", attrs = {"class":"color-list"})
for ürün in ürünler:
  ürün_linkleri = ürün.find_all("a", attrs={"class":"tw"})
  for link in ürün_linkleri:
    counter+=1
    renkkodu = link.get("href")
    renkkodu = renkkodu.strip("/")
    renkadi = link.text.strip()
    renkListesi=[]
    renkListesi.append((renkadi,convertHexToDecimal(renkkodu)))#renk kodu burada 10luk sisteme dönüştürülmelidir ve şuanda 16lık sistemdedir.
    

ans = ""
input_r = -1
input_g = -1
input_b = -1

while ans != "h":
  sys.stdout.flush()
  input_r = int(input("lutfen RGB değerinin Red değerini giriniz.(0-255)"))

  input_g = int(input("lutfen RGB değerinin Green değerini giriniz.(0-255)"))
  
  input_b = int(input("lutfen RGB değerinin Blue değerini giriniz.(0-255)"))

  input_rgb =[input_r,input_g,input_b]
  EnYakinRenk = enYakinBenzerlikOraniBul(input_rgb,renkListesi)
  print(EnYakinRenk)

  


  print("devam etmek istiyor musunuz? -(e/h)-")
  ans = input()
  
  input_r = -1
  input_g = -1
  input_b = -1
