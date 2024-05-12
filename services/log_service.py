#import libraries
from datetime import datetime
#Write logs into log.txt file
def log_progress(message):
    """This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing"""

    with open('log/log.txt', 'a') as f:
        f.write(f'{datetime.now()}: {message}\n')