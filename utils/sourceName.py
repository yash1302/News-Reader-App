import re
from utils import logger
import tldextract


def source_name(link: str) -> str:
    """it takes the URL and return media Name

    Args:
        link (str): URL of the website

    Returns:
        str: Media name
    """
    try:
        func_name = re.findall(
            r"[a-zA-Z0-9]+\.[a-zA-Z]+/", link)
        # func_name = tldextract.extract(link).domain
        func_name = func_name[0].split(".")[0]
        logger.logMessage("source name is identified")
        return func_name
    except Exception as e:
        logger.logException(e)

