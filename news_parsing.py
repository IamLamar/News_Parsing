import csv
from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning

def parse():
     requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
     r = requests.get(url ='https://24.kg/',verify=False)
     soup = BeautifulSoup(r.content,'html.parser')
     items = soup.find_all('div',class_ ='title')
     new_list = []
     for i in items:
          new_list.append({
               "заголовок": i.get_text(strip=True)
          })
     return new_list
result = parse()
print(result)




          




