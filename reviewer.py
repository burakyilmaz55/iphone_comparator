import requests
from bs4 import BeautifulSoup


def n11():
    url= "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?m=Apple"
    html = requests.get(url).content
    soup = BeautifulSoup(html,"html.parser")


    list = soup.find_all("li", {"class":"column"})

    for li in list:
        name = li.div.a.h3
        link = li.div.a.get("href")
        new_price = li.find("div",{"class":"proDetail"}).find("a",{"class":"newPrice"})
        print(f"Cihaz Adı: {name.text.strip()}\nFiyatı: {new_price.text}\nLink: {link}")

n11()