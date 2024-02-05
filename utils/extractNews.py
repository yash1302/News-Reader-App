import bs4
import requests
from utils import logger

scrappedDataDict = {
    "Heading" : "",
    "overview" : ""
}

def foxnews(Link:str)->dict :
    """this function takes link as argument and return heading and body in dictionary form

    Args:
        Link (str): URL of the website

    Returns:
        dict: it contains heading and title
    """
    try:
        response = requests.get(Link)
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        scrappedDataDict['Heading'] = (soup.find('h1', attrs={'class':'headline speakable'}).text)
        logger.logMessage("heading of foxnews has been scrapped ")
        text = soup.find_all('div', attrs={'class':'article-content-wrap sticky-columns'})
        logger.logMessage("text from foxnews has been scrapped")
        scrappedDataDict['overview'] = (text[0].text)

        return scrappedDataDict
    except Exception as e:
        logger.logException(e)

def who(Link:str)->dict:
    response = requests.get(Link)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    scrappedDataDict['Heading'] = soup.find('h1').text
    logger.logMessage("heading of who has been scrapped ")

    text = soup.find_all('article', attrs={'class':'sf-detail-body-wrapper'})
    logger.logMessage("text from who has been scrapped")
    
    scrappedDataDict['overview'] = text[0].text

    return scrappedDataDict
