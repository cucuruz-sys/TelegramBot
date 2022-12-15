from bs4 import BeautifulSoup
import requests
import json


def proh_ball_func():
    main_url = "https://priem.pgups.ru/doc_passmark.php"
    req = requests.get(main_url)
    soup = BeautifulSoup(req.text, "html.parser")

    proh_ball = []
    table = soup.find('table', attrs={'class':'table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        proh_ball.append([ele for ele in cols if ele])
    return proh_ball


