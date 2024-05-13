#import libraries
from services.log_service import log_progress
import requests
import json
import pandas as pd

#Extract Data
def extract(url):
    log_progress('Data Extraction Started')
    """ This function aims to extract the previously scraped daraz liquor
    information from the github and save it to a data frame. The
    function returns the data frame for further processing. """
    resp = requests.get(url)
    data = [json.loads(line) for line in resp.text.splitlines()]
    df = pd.DataFrame(data)
    log_progress('Data Extraction Completed')
    return df