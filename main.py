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
        final_data = []
        for link in json_loaded:
            function_name = sourceName.source_name(link)
            logger.logMessage("source name has been fetched")
            func = getattr(extractNews, function_name)
            logger.logMessage("heading and body is scrapped")
            final_data.append(func(link))
            logger.logMessage("added into dictionary")
        # print(final_data)
        with open('output.txt', 'w', encoding='UTF-8') as f:
            for row in final_data:
                f.write(str('Link - ' + str(row['Link'] + "\n")))
                f.write(str('Heading - ' + str(row['Heading'] + "\n")))
                f.write(str('overview - ' + str(row['overview'] + "\n\n")))

        # json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
        # str_data = str(final_data)
        # with open("output.txt", "w",encoding="UTF-8") as outfile:
        #     for news in final_data:
        #         outfile.write("link --> " + str(news[link]))
        # for news in final_data:
        #     print(news[link])
        

    except Exception as e:
        logger.logException(e)

    
if __name__ == "__main__":
    main()