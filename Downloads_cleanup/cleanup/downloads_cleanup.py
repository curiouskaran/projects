import os
import glob

__name__ = 'downloads_cleanup.py'
__author__ = 'Karan sharma'

'''moves files from /Downloads to correct respective directories automaticaly
with help of cronjob that initiates itself every hour'''

home = os.getenv('HOME')

