'''
This module contains the functions to retrieve data from urls
'''

import numpy as np
import pandas as pd
import requests
from urllib.parse import urljoin
import os
import logging
import sys

sys.path.append('./src/')

from auth import *

# To not show username and password the variables GITHUB_USERNAME and GITHUB_PASSWORD
# are stored in a separate file that are not push remotely
AUTH = (GITHUB_USERNAME, GITHUB_TOKEN)

logging.basicConfig(level=logging.INFO)

def retrieve_data_from_url(base_url, conditions=[], start_page=1, max_page=100):
    '''
    Retrieves the data from a url
    
    Args:
        - start_page (int): the number of the page from which we want to start collecting
        (used when we want to restart a stopped retrieving)
        - max_page (int): maximum number of pages we wnat collect the data from
        
    Returns:
        - array_total_data (array): Contains all the data in the form of Dictionaries
    '''
    
    array_total_data = []  # array that contains all the repos in the form of a Dict
    logging.info(f"Starting retrieving data from {base_url}")
    page=start_page
    while True:
        json_data = request_json_page_data(base_url=base_url, conditions=conditions, page=page, per_page=100)     
        if len(json_data)==0 or page>max_page:
            break 
        for repo in json_data:
            array_total_data.append(repo)
        logging.info(f"Retrieved data from page {page}")
        page+=1
        
    return array_total_data

def request_json_page_data(base_url, conditions, page, per_page):
    '''
    Retrieves the data of one page
    
    Args:
        - base_url (str): the base url without the pagination part 
        (the url of the organization github where the repositories are listed)
        - page (int): the number of the page from which we want to retrieve data
        - per_page (int): number of repos we want to retrieve from the page
        - sort_per_name (bool): if True sorts the repos by name
        
    Returns:
        - json_data (array): Contains the data retrieved from the url in form of a dictionary
    '''
    url_page = f"{base_url}?per_page={per_page}&page={page}"
    for condition in conditions:
        condition_string = "&" + condition
        url_page += condition_string
    response = send_request(url_page, auth=AUTH)
    json_data = response.json()
    
    return json_data

def send_request(url, auth):
    '''
    Performs a request to a certain url
    
    Args:
        - url (str): the url from which we want to retrieve data
        - auth (str, str): in the from of (username, password). Used to authenticate the request
        
    Returns:
        - response (Response): containse the response of the request
    '''
    response = requests.get(url, auth=AUTH, timeout=10)
    response.raise_for_status()
    if response.status_code!=200:
        msg = f"Unexpected exception occurred with status code {response.status_code}.\n"
        msg += f"The suspected reason was {response.reason}"
        raise ValueError(msg)
    
    return response
    
    
def main():
        base_url = "https://api.github.com/repos/google/jax/commits"
        data = retrieve_data_from_url(base_url,1, 1000)
        print(data[0])
    
if __name__=="__main__":
    main()
    
    