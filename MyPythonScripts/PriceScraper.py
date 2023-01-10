import bs4, requests

def getEbayPrice(productUrl):
    
    res=requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()






price=getEbayPrice('https://www.ebay.com/itm/261501565606?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20200708143445%26meid%3D7f10bbf0357b481091404410f6367fb9%26pid%3D101251%26rk%3D1%26rkt%3D1%26itm%3D261501565606%26pmt%3D0%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithMoreCoviewRecall%26brand%3DSTMicroelectronics&_trksid=p2380057.c101251.m47269&_trkparms=pageci%3A339c14a7-5e34-11ec-86ae-b2f05104ae61%7Cparentrq%3Ac1cb927e17d0ab97d1d17019fff56472%7Ciid%3A1')
print('The price is ' + price)
