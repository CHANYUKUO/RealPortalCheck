from bs4 import BeautifulSoup
import re
import requests
import time;

localtime = time.localtime(time.time())
mon=localtime.tm_mon
day=localtime.tm_mday

def Search():
    import requests

    cookies = {
    }

    headers = {
    }

    response = requests.get('https://real-app.ucsd.edu/opportunities', headers=headers, cookies=cookies)

    soup = BeautifulSoup(response.text,"html.parser")
    subSoup= soup.find_all("div", {"class": "posted-today"})## find the class name "this-week"
    variable=[];index=0;
    for div in subSoup:
        variable=div.find_all("div",{"class": "preview-title full"})
    for individual in variable:
        text = str(individual)
        variable[index]=text[32:len(text)-6]
        index+=1
    return variable



if __name__ == '__main__':
    result = Search() 
    if result == []:
        print('No new Uploads today')
    else:
        print('There are '+ str(len(result))+ ' results today')
        for text in result:
            print(text)
    input()
