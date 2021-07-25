import requests    #用request跟伺服器聯絡
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'

r = requests.get('https://disp.cc/b/NEWS')
soup = BeautifulSoup(r.text, 'html.parser')    #用html的解析器解析 r裡面的一堆文字
print(soup)
spans = soup.find_all('span', class_='listTitle')     #find_all（裡面是搜尋的條件filter）
for span in spans:
	href = span.find('a').get('href')
	if href == '50-OE' :
		break
	if href == '163-7gWH':
		break
	url = root_url + href
	title = span.text
	print(f'{title}\n{url}')
	#print(span.text)    #拿span裡面的text
	#print(span.find('a').get('href'))    #每一個spans裡面還可以find(XX條件) ; 拿href身上的屬性  ;用字典也可['href']
