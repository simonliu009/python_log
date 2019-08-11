#-*- coding: utf-8 -*-

import log
import sys,os,datetime

log = log.Log(filename='111.log', mode='a', cmdlevel = 'DEBUG', filelevel = 'INFO', limit= 20480, backup_count = 10, colorful = True)
log.debug('This is a debug level message')
log.info('This is a info level message')
log.warning('This is a warning level message')
log.error('This is a error level message')
log.critical('This is a critical level message')


now = datetime.datetime.utcnow()
oneMinuteAgo = (datetime.datetime.utcnow() - datetime.timedelta(minutes = 1))
timestr1 = now.strftime("%Y%m%d%H%M")
timestr2 = oneMinuteAgo.strftime("%Y%m%d%H%M")
log.info('Now:%s',timestr1)
log.info('One Minute Ago:%s',timestr2)
