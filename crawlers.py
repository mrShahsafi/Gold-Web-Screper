from confs import SOURCE_SITE
from bs4 import BeautifulSoup as crawler
from requests import get as get_req

def tgju_creawler():
    res = get_req(SOURCE_SITE)
    if res.status_code != 200:
        return None
    page = crawler(
        res.content,
        "html.parser",
    )
    
    coint_table = page.find(
        "table",
        id='coin-table'
    ) 
    data = ''
    for row in coint_table.find_all("tr"):
        if len(row.contents) == 11:
            title = row.find("th")
            price = row.find('td')
            data = data + f"{title.text}:{price.text}\n"
    
    return data

    
