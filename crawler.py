__author__ = 'Xiang'


import urllib2
from bs4 import BeautifulSoup
import os
import time
from random import randint


# define the base url and default directory
BASE_URL = 'http://www.imdb.com'
TOP_250 = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'
DIR = 'data'


def get_movie_link(url):
    """
    :param url: url from the top250 movie list
    :return: url of the web that contains the movie synopsis
    """
    url = BASE_URL + url
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    div = soup.find(class_='article', id='titleStoryLine')
    span = div.find_all('span', class_='see-more inline')
    link = span[0].a['href']
    return link


def get_movie_syno(url):
    """
    :param url: url of the web that contains movie synopsis
    :return: parsed movie synopsis
    """
    url = BASE_URL + get_movie_link(url)
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    content = soup.find_all(class_='ipl-zebra-list', id='plot-synopsis-content')

    # content[0] contains the movie synopsis under tage li
    return content[0].li.get_text()


def main():
    """
    Parse the synopses for movies in the top250 list and write titles and
    synopses to files under the data directory
    """
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    synopses = open(DIR + '/' + 'synopses.txt', 'w')
    titles = open(DIR + '/' + 'titles.txt', 'w')

    # Start from the web of top250 movie list, TOP_250 url
    response = urllib2.urlopen(TOP_250)
    soup = BeautifulSoup(response.read(), 'lxml')

    # items contains the links of the all 250 movies
    items = soup.select('.lister-list .titleColumn')
    start_time = time.time()

    for i, item in enumerate(items):
        title = item.find('a').get_text().encode('utf-8')
        link = item.find('a')['href']
        synopsis = get_movie_syno(link).encode('utf-8')

        # control the rate of crawling
        time.sleep(randint(1, 6))
        titles.write('%s\n' % title)
        synopses.write('%s\n BREAKS HERE\n' % synopsis)

        # monitor the crawling status
        if i % 10 == 0:
            print '%d web crawled and elapsed time: %fs' % (i + 1, time.time() - start_time)
    synopses.close()
    titles.close()


if __name__ == '__main__':
    main()
