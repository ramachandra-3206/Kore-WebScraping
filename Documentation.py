from bs4 import BeautifulSoup
import requests
def getLinks(url):
    response = requests.request('get',url).text
    soup = BeautifulSoup(response, 'html.parser')
    anchors = soup.find_all('a')
    for anchor in anchors:
        link = anchor.get('href')
        if link == None:
            print("===================")
            print(anchor)
            print("===================")

        print(link)

getLinks("https://developer.kore.ai")