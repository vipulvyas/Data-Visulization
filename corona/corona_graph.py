import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    if int(sys.argv[1]) == 1:
        print('\n')
        print(os.system("clear && figlet 'CORONA LIVE STATUS IN INDIA' -f digital -c"))

        print('\n')
        extract_contents = lambda row: [x.text.replace('\n','') for x in row]

        URL = 'https://www.mohfw.gov.in/'
        print("Ref. Data: "+ URL + "\n")
        SHORT_HEADERS = ['SNo','State','Indian-Confirmed','Foreegn-Confirmed','Cured','Death']
        response = requests.get(URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = extract_contents (soup.tr.find_all('td'))
        stats = []
        all_rows = soup.find_all('tr')
        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            if stat:
                if len(stat) == 5:
                    stat = ['',*stat]
                    stats.append(stat)
                elif len(stat) == 6:
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
        plt.barh(y_pos, performance , align='center', alpha=0.5, color=(234/256.0, 128/256.0, 252/256.0),edgecolor=(106/256.0,27/256.0,154/256.0))
        plt.yticks(y_pos, objects)
        plt.xlim(1,200,1)
        plt.xlabel('Number of Cases')
        plt.title('Corona virus status')
        plt.show()
    if int(sys.argv[1]) == 2:
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
        print("\tC = Contry\n\tTC = Total Cases\n\tNC = New Cases\n\tTD = Total Death\n\tND = New Death\n\tTR = Total Recoverd\n\tAC = Active Cases\n\tS = Serious\n\tTC/1Mp = TotCases/1M pop\n\tD/1Mp = Death/1M pop\n\t1s = 1st Case\n")
       
        
        SHORT_HEADERS = ['C','TC','NC','TD','ND','TR','AC','S','TC/1Mp','D/1Mp','1s']
        response = requests.get(URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = extract_contents (soup.tr.find_all('td'))
        stats = []
        all_rows = soup.find_all('tr')
        for row in all_rows:
            stat = extract_contents(row.find_all('td'))
            if stat:
                #if len(stat) ==11:
                stat = ['',*stat]
                stats.append(stat)
                # elif len(stat) == 6:
                #     stats.append(stat)

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
        plt.barh(y_pos, performance , align='center', alpha=0.5, color=(234/256.0, 128/256.0, 252/256.0),edgecolor=(106/256.0,27/256.0,154/256.0))
        plt.yticks(y_pos, objects)
        plt.xlim(1,200,1)
        plt.xlabel('Number of Cases')
        plt.title('Corona virus status')
        plt.show()



