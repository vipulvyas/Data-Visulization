import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# world //*[@id="main_table_countries_today"]
# Europe /html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]
# North America /html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/tbody[1]


if __name__ == "__main__":
    if sys.argv[1] == '-h':
        print('Usege:\n\tINDIA STATUS : python3 test_np.py 1 \n\tWORLD STATUS : python3 test_np.py 2\n')
    elif int(sys.argv[1]) == 1:
        print('\n')
        print(os.system("clear && figlet 'CORONA LIVE STATUS IN INDIA' -f digital -c"))

        print('\n')
        extract_contents = lambda row: [x.text.replace('\n','') for x in row]

        URL = 'https://www.mohfw.gov.in/'
        print("Ref. Data: "+ URL + "\n")
        #SHORT_HEADERS = ['SNo','State','Indian-Confirmed','Foreegn-Confirmed','Cured','Death']
        SHORT_HEADERS = ['SNo','State','Cases','Cured','Death']
        response = requests.get(URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = extract_contents (soup.tr.find_all('td'))
        stats = []
        all_rows = soup.find_all('tr')
        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            if stat:
                if len(stat) == 4:
                    stat = ['',*stat]
                    stats.append(stat)
                elif len(stat) == 5:
                    stats.append(stat)

        #stats[-1][1] = "Total Cases"
        #stats.remove(stats[-1])
        objects = []
        for row in stats:
            objects.append(row[1])
        y_pos = np.arange(len(objects))
        performance = []
        for row in stats:
            performance.append(str(row[2]) + str(row[3]))

        table = tabulate(stats, headers = SHORT_HEADERS)
        print(table)
        print('\n')
        print('\n')
        print('\n')
        i=0
       
    elif int(sys.argv[1]) == 2:
        print('\n')
        print(os.system("clear && figlet 'CORONA LIVE STATUS IN WORLD' -f digital -c"))

        print('\n')
        URL = 'https://www.worldometers.info/coronavirus/'
        try:
            if sys.argv[2]:
                pass
        except Exception:
            pass
        extract_contents = lambda row: [x.text.replace('\n','') for x in row]
        print("Ref. Data: "+ URL +"\n")
        print("\tC = Contry\tTC = Total Cases\tNC = New Cases\tTD = Total Death\tND = New Death\tTR = Total Recoverd\tAC = Active Cases\tS = Serious\n\tTC/1Mp = TotCases/1M pop\tD/1Mp = Death/1M pop\t1s = 1st Case\n")
       
        
        SHORT_HEADERS = ['C','TC','NC','TD','ND','TR','AC','S','TC/1Mp','D/1Mp','Test/1Mp','Test D/1Mp']
        response = requests.get(URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = extract_contents (soup.tr.find_all('td'))
        stats = []
        all_rows = soup.find_all('tr')
        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            try:
                if row.td['data-continent'] == "Europe" :
                    print("hello\n\n\n")
            except:
                pass
            if stat:
                stat = ['',*stat]
                stats.append(stat)
        # objects = []
        # for row in stats:
        #     objects.append(row[1])
        # y_pos = np.arange(len(objects))
        # # print(y_pos)

        table = tabulate(stats, headers = SHORT_HEADERS)
        print(table)
        print('\n')
        print('\n')
        print('\n')
    else:
        print('Usege:\n\tINDIA STATUS : python3 test_np.py 1 \n\tWORLD STATUS : python3 test_np.py 2\n')            
