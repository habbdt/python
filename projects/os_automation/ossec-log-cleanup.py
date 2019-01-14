#!/usr/bin/env python

import os
import time
import re
import logging


# delete any files older than 13 months or 400 days

timespan = 86400*400
now = time.time()


for root, dirs, files in os.walk('/var/ossec/logs/alerts'):
    for filename in files:
        path = os.path.join(root, filename)
        match = re.search(r'\d\d\d\d', path)
        if match:
            timestamp = os.path.getmtime(path)
            timev = now - timespan
            if timev > timestamp:
                try:
                    logging.basicConfig(filename='/var/log/ossec_cleanup.log',
                                        level=logging.INFO)
                    os.remove(path)
                    logging.info("Removed files %s, timestamp is %s", path, now)
                except Exception, e:
                    logging.basicConfig(filename='/var/log/ossec_cleanup.log',
                                        level=logging.ERROR)
                    logging.error("Unable to remove file %s", path)
                    pass
