from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs4

class Schedule():

    arrivals = []
    departures = []

    def __init__(self, code: str):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options = options)
        url = 'https://www.flightradar24.com/data/airports/' + code.lower()
        driver.get(url)
        driver.implicitly_wait(30)
        driver.find_element(By.CLASS_NAME, 'cell-airline')
        html = driver.page_source
        soup = bs4(html, 'lxml')
        tables = soup.find_all('table', attrs={'class':'table table-condensed table-hover data-table m-n-t-15'})
        self.arrivals = self.fetch_flightdata(tables[0])
        self.departures = self.fetch_flightdata(tables[1])

    def fetch_flightdata(self, table):
        rows = table.find_all('tr')
        dataList = []

        for row in rows:
            elements = row.find_all('td')
            if len(elements)<5:
                continue
            scheduleTime = elements[0].get_text()
            flight = elements[1].find('a', attrs={'class':'notranslate ng-binding'}).get_text()
            location = elements[2].get_text()[:-1]
            airline = elements[3].find('a').get_text()[:-1]
            aircraft = elements[4].find('span').get_text()
            status = elements[6].get_text()
                
            data = {
                'time' : scheduleTime,
                'flight' : flight,
                'location' : location,
                'airline' : airline,
                'aircraft' : aircraft,
                'status' : status
            }

            dataList.append(data)

        return dataList