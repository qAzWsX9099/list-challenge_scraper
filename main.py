import requests
# import pandas
from bs4 import BeautifulSoup
def main():
    # print("hello, world!")

    url = 'https://www.listchallenges.com/beginner-socialistcommunist-reading-list'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    web_page_count = len(soup.find(attrs={"class": "pager"}).contents)
    
    for item_name in soup.find_all(attrs={"class": "item-name"}):
        print(item_name.get_text(strip=True))


# get number of class=pager
# add "/list/i" to url





web_page_count = len(soup.find(attrs={"class": "pager"}).contents)









if __name__ == "__main__":
    main() 