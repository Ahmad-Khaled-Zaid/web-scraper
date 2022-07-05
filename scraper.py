import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    para_cards = soup.find_all("p")
    counter = 0
    for para in para_cards:
        span = para.find_all('span')
        if span:
            counter += len(span)
    return counter


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    para_cards = soup.find_all("p")
    need_citation = ""
    for para in para_cards:
        span = para.find_all('span')
        if span:
            need_citation += "-" + para.contents[0].strip() + '\n'
    return need_citation


report = get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
print(report)
print(f'the number of citations needed is {get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")}')
