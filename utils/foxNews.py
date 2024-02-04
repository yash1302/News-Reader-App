import bs4
import requests

scrappedDataDict = {}

def foxNews(URL:str)->dict :
    response = requests.get(URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    scrappedDataDict['Heading'].extend(soup.find('h1', attrs={'class':'headline speakable'}).text)

    text = soup.find_all('div', attrs={'class':'article-content-wrap sticky-columns'})
    
    scrappedDataDict['overview'].extend(text[0].text)

    return scrappedDataDict


