from bs4 import BeautifulSoup
import requests

main_url = "https://priem.pgups.ru/doc_passmark.php"
req = requests.get(main_url)
soup = BeautifulSoup(req.text, "html.parser")

data = []
table = soup.find('table', attrs={'class':'table'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print (data)