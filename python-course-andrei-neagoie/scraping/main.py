import requests
from bs4 import BeautifulSoup
import pprint


def get_links_and_subtext(page):
    res = requests.get(f"https://news.ycombinator.com/news{f'?p={page}' if page >= 2 else ''}")
    # parse data from html, beautiful soup can parse other types of data as well as like xml
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select(".titlelink")
    subtext = soup.select(".subtext")
    return {"links": links, "subtext": subtext}


def sort_stories_by_votes(hacker_news):
    # by which you want to sort by
    # lambda func will receive each dictionary in list
    return sorted(hacker_news, key=lambda k: k["votes"], reverse=True)


def create_custom_hacker_new(hacker_links, hacker_subtext):
    hn = []
    for idx, item in enumerate(hacker_links):
        # enumerate also returns the index as first value of tuple
        title = hacker_links[idx].getText()
        href = hacker_links[idx].get("href", None)  # second one is default
        vote = hacker_subtext[idx].select(".score")
        if len(vote):
            # vote is actually a list with single element
            points = int(vote[0].getText().replace(" points", ""))
            if points >= 100:
                hn.append({"title": title, "href": href, "votes": points})
    return sort_stories_by_votes(hn)


links_and_subtext = get_links_and_subtext(19)
pprint.pprint(create_custom_hacker_new(links_and_subtext["links"], links_and_subtext["subtext"]))
