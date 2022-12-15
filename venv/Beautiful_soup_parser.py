from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import json


def proh_ball_func():
    main_url = "https://priem.pgups.ru/doc_passmark.php"
    req = requests.get(main_url)
    soup = BeautifulSoup(req.text, "html.parser")

    proh_ball = []
    table = soup.find('table', attrs={'class': 'table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        proh_ball.append([ele for ele in cols if ele])
    return proh_ball


def napr_podg_func(fac, forma):
    main_url = "https://priem.pgups.ru/src/specialization.php"

    HEADERS = {

    }
    DATA = {
        'submitted': 1,
        'form': [],
        'fclt': [],
        'cost': '30000,130000'
    }

    if (fac == 1):
        DATA['fclt'].append("Автоматизация и интеллектуальные технологии")
    elif (fac == 2):
        DATA['fclt'].append("Промышленное и гражданское строительство")
    elif (fac == 3):
        DATA['fclt'].append("Транспортное строительство")
    elif (fac == 4):
        DATA['fclt'].append("Транспортные и энергетические системы")
    elif (fac == 5):
        DATA['fclt'].append("Управление перевозками и логистика")
    elif (fac == 6):
        DATA['fclt'].append("Факультет безотрывных форм обучения")
    elif (fac == 7):
        DATA['fclt'].append("Экономика и менеджмент")
    else:
        print("Code fac not found")

    DATA['form'].append(forma)

    req = requests.get(main_url, headers=HEADERS, params=DATA)
    soup = BeautifulSoup(req.text, 'html.parser')

    res = []
    for x in soup.findAll("div", class_="education__card education__color-1"):
        temp = []

        temp.append(x.find("div", class_="education__name").text.strip())
        temp2 = []
        for el in range(3):
            temp2.append(x.find("div", class_="collapse").findAll("span", class_="education__badge")[el].text.strip())
        temp.append(temp2)
        #temp.append(x.find("div", class_="col-lg-2 col-md-2 col-xs-2 text-right").find("span", class_="education__badge").text.strip())
        temp.append(x.find("div", class_="col-lg-6 col-md-6 col-xs-6 text-right").find("span", class_="education__badge").text.strip()[:len(x.find("div", class_="col-lg-6 col-md-6 col-xs-6 text-right").find("span", class_="education__badge").text.strip())-2])
        res.append(temp)
    return res



def sdan_ekz_func(ekz):
    main_url = "https://priem.pgups.ru/src/specialization.php"

    HEADERS = {

    }
    DATA = {
        'submitted': 1,
        'vi':[],
        'cost': '30000,130000'
    }


    DATA['vi'].append(ekz)

    req = requests.get(main_url, headers=HEADERS, params=DATA)
    soup = BeautifulSoup(req.text, 'html.parser')

    res = []
    for x in soup.findAll("div", class_="education__card education__color-1"):
        temp = []

        temp.append(x.find("div", class_="education__name").text.strip())
        temp2 = []
        for el in range(3):
            temp2.append(x.find("div", class_="collapse").findAll("span", class_="education__badge")[el].text.strip())
        temp.append(temp2)
        #temp.append(x.find("div", class_="col-lg-2 col-md-2 col-xs-2 text-right").find("span", class_="education__badge").text.strip())
        temp.append(x.find("div", class_="col-lg-6 col-md-6 col-xs-6 text-right").find("span", class_="education__badge").text.strip()[:len(x.find("div", class_="col-lg-6 col-md-6 col-xs-6 text-right").find("span", class_="education__badge").text.strip())-2])
        res.append(temp)
    return res