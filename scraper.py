import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys


def get_data():
    res = requests.get('https://imdb-api.com/en/API/BoxOfficeAllTime/k_pv17fc8j')
    soup = BeautifulSoup(res.text, 'lxml')
    soup = str(soup).strip('</p></body></html>')
    soup = soup.strip('{"items":')
    soup = soup.strip(',"errorMessage":""}')
    json1 = eval(soup)
    return json1


if __name__ == '__main__':
    movies = get_data()
    df = pd.DataFrame(movies)
    if len(sys.argv) == 1:
        print(movies)
    elif sys.argv[1] == '--scrape':
        print(df.head(int(sys.argv[-1])))
    else:
        df.to_csv(str(sys.argv[-1]), index=False)

