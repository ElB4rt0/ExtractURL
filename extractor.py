#!/usr/bin/python
# -*- coding: utf-8 -*- 
__version__ = "1.5"
__author__  = "elbarto"
import requests
from bs4 import BeautifulSoup
import argparse
import re


class bcolors:
    OKBLUE = '\033[94m'
    OKWHITE = '\033[37m'
    GREEN = '\033[32m'
    FAIL = '\033[91m'

def banner():
    print """                           
  |\/\/\/\/\/|
  |          |
  |          |       .------------------------.
  |          |      |                         |
  |    __  __|      | EAT MY SHORTS SYSADMIN! |
  |   /  \/  \      |                         |
  |  (o   )o  )    /_-------------------------'
 /C   \__/ --.
 \_   ,     -'
  |  '\_______)
  |      _)        Developer :elbartopwn@protonmail.com
  |     |          GitHub: https://github.com/ElB4rt0 | collaborator : https://github.com/dplastico
 /`-----'\ 
    """
def findinglinks (soup):
    for link in soup.find_all('a'):
    	    obtain = link.get('href', '')
            if 'http' in obtain:
                print bcolors.FAIL + "[URL] " + bcolors.OKWHITE + obtain
list_1 = []
newlist = []
def findingdirectories(soup):
  links2 = soup.find_all('a', href=re.compile("^(/)"))
  for link_1 in links2:
    list_1.append(link_1['href'])
    for i in set(list_1):
        if i not in newlist:
            newlist.append(i)
def main ():
    parser = argparse.ArgumentParser(description="HELP MENU\n  Extract all the URL in a given link", version=__version__)
    parser.add_argument("-u", "--url", help="URL to scan, url example http://domain.com or https://www.domain.com", required=True)
    parser.add_argument("-s","--skipssl", help="Use to skip SSL verification", action='store_true')
    parser.add_argument("-d","--directories", help="Listing Directories", action="store_true")
    args = parser.parse_args()
    if args.url:
        url = args.url
    if url.endswith('/'):
        url = url[:-1]
    session = requests.session()
    if args.skipssl:
        http = session.get(url, verify=False)
    else:
        http = session.get(url,)
    soup = BeautifulSoup(http.text, "html.parser")
    banner()
    findinglinks(soup)
    if args.directories:
        findingdirectories(soup)
        for a in newlist:
            print bcolors.FAIL + "[Directories] " + bcolors.OKWHITE + url + a
if __name__ == '__main__':
    main()
