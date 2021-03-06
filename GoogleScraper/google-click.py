# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError
import click

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

lb = "+--------------------------------------------------------------+"
# prefix of search term
site = "site:vodlocker.com "
# ask user for search term


@click.command("search_google" , short_help="Search google for your film.")
@click.option("--title", prompt=site + input("{0}\n|{1}[?] {2}Enter a film title to search for..\n|\n|{3}--> {4}".format(lb, O, W, B, W)), help="An option to add a film title to search to cli.")  
@click.argument("title", metavar="<title>")     
def search_google():
    """A function to search google for our film
    """
    #prompt = site + input("{0}\n|{1}[?] {2}Enter a film title to search for..\n|\n|{3}--> {4}".format(lb, O, W, B, W))
    keywords = prompt
    config = {
    'use_own_ip': True,                     # whether to use our own IP address 
    'keyword': keywords,
    'search_engines': ['google'],           # various configuration settings
    'num_pages_for_keyword': 1,
    'scrape_method': 'http',
    'do_caching': False,
    'num_results_per_page': 50,
    'log_level': 'CRITICAL',
    'output_filename': 'results.csv'        # file to save links to 
#    'proxy_file': 'proxies.txt'            # file to load proixies from 
    }
    try:
        search = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)

search_google()        
print("searched", prompt)
