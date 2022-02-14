from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Accept-Language':'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'}
url="https://www.amazon.com/SanDisk-1TB-Extreme-Portable-SDSSDE61-1T00-G25/dp/B08GTYFC37/ref=sr_1_5?qid=1637746974&qsid=135-2839638-0160146&s=computers-intl-ship&sr=1-5&sres=B07CRG94G3%2CB0815XFSGK%2CB08164VTWH%2CB07MFZXR1B%2CB08GTYFC37%2CB08K3S6WJM%2CB08QBMD6P4%2CB08HN37XC1%2CB06W55K9N6%2CB07MJW5BXZ%2CB078211KBB%2CB07STGGQ18%2CB08166SLDF%2CB08V83JZH4%2CB07H2RR55Q%2CB01N5IB20Q%2CB0143UM4TC%2CB08GLX7TNT%2CB095HB3L6G%2CB073SBQMCX"
response=requests.get(url,headers=headers)
data=response.text

soup=BeautifulSoup(data,'lxml')
print(soup.find(name="span", id="priceblock_ourprice"))