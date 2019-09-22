#My solution
from datetime import datetime
from datetime import timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

#for you to code:
def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    datetime_part = line.split()
    datetime_part = datetime_part[1]
    date,time = datetime_part.split('T')
    year, month, day = date.split('-')
    year, month, day = int(year), int(month), int(day)
    hour, minute, second = time.split(':')
    hour, minute, second = int(hour), int(minute), int(second)
    return datetime(year, month, day, hour, minute, second)

def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    timedelta_list = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            timedelta_list.append(convert_to_datetime(line))
    timediff = (timedelta_list[-1] - timedelta_list[0])
    return timediff

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)
with open(logfile) as f:
    loglines = f.readlines()
    time_between_shutdowns(loglines)

# ACTUAL SOLUTION

from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    timestamp = line.split()[1]
    date_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(timestamp, date_str)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    return max(shutdown_times) - min(shutdown_times)
