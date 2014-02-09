mySQLHandler
============

[python] logginghandler for MySQL

 Based on Vinay Sajip's DBHandler class (http://www.red-dove.com/python_logging.html)
forked from ykessler/gae_handler.py (https://gist.github.com/ykessler/2662203)
<from ykessler/gae_handler.py>
This version sacrifices performance for thread-safety:
Instead of using a persistent cursor, we open/close connections for each entry.
AFAIK this is necessary in multi-threaded applications,
because SQLite doesn't allow access to objects across threads.
</from>

<from onemoretime>
please see https://github.com/onemoretime/mySQLHandler for more up-to-date version
a lot of things to do : create SQL table if necessary, try/except when execute sql, auto-connect to db...
</from>

Prerequisites:
a db user, typically 'logger' with following privileges on mysql db, typically 'logger'

Usage:

import logging
import mySQLHandler

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

db = {'host':'localhost', 'port': 3306, 'dbuser':'logger', 'dbpasswd':'loggerpasswd', 'dbname':'logger'}

sqlh = mySQLHandler.mySQLHandler(db)
logger.addHandler(sqlh)


logger.info('info')
logger.debug('debug')

Other examples and multithreaded examples:
See log_examples.py
