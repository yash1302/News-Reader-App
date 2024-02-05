import json
from utils import extractNews,sourceName,logger
def main():
    """main
    """
    try:
        final_data = {}
        with open("config.json","r") as file:
            json_loaded = json.load(file)
        logger.logMessage("input from Json file is loaded")
        for link in json_loaded:
            function_name = sourceName.source_name(link)
            logger.logMessage("source name has been fetched")
            func = getattr(extractNews, function_name)
            logger.logMessage("heading and body is scrapped")
            final_data[link] = (func(link))
            logger.logMessage("added into dictionary")
        json_object = json.dumps(final_data, indent=4)
        with open("output.txt", "w") as outfile:
            outfile.write(json_object)

    except Exception as e:
        logger.logException(e)

    
if __name__ == "__main__":
    main()