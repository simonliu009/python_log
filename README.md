# python_log

用法：
```python
import log

log = log.Log(filename='111.log', mode='a', cmdlevel = 'INFO', filelevel = 'INFO', limit= 20480, backup_count = 10, colorful = True)
log.debug('This is a debug level message')
log.info('This is a info level message')
log.warning('This is a warning level message')
log.error('This is a error level message')
log.critical('This is a critical level message')
```


