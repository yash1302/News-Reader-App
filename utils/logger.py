import logging

logging.basicConfig(filename='logfile.log' , format='%(asctime)s - %(message)s', level=logging.INFO)

def logMessage(text:str): 
    """This function logs the information

    Args:
        text (str): it takes log message
    """
    logging.info(text)

def logException(text:str):
    """this function is used to log the exception which happened

    Args:
        text (str): we pass exception as parameter
    """
    logging.error(text)