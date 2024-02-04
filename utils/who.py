import bs4
import requests

scrappedDataDict = {}

def who(URL:str)->dict:
    response = requests.get(URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    scrappedDataDict['Heading'].extend(soup.find('h1').text)

    text = soup.find_all('article', attrs={'class':'sf-detail-body-wrapper'})
    
    scrappedDataDict['overview'].extend(text[0].text)

    return scrappedDataDict