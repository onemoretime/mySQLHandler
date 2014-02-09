# -*- coding: utf-8 -*-
'''
@author: john
@credits: http://www.tutorialspoint.com/python/python_multithreading.htm
'''
import threading
import Queue
import time
import logging
import mySQLHandler

exitFlag = 0

class myThread_basic (threading.Thread):
    def __init__(self, log,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.log = log
    def run(self):
        self.log.info("Starting " + self.name)
        print_log(self.log,self.name, self.counter, 5)
        self.log.info( "Exiting " + self.name)

class myThread_priorizedqueue (threading.Thread):
    def __init__(self, log,threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.log = log
    def run(self):
        self.log.info("Starting " + self.name)
        process_log(self.log,self.name, self.q)
        self.log.info( "Exiting " + self.name)

class myThread_sync (threading.Thread):
    def __init__(self, log,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.log = log
    def run(self):
        self.log.info("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        print_log(self.log,self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

def process_log(log,threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            log.info("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

def print_log(log,threadName, delay, counter):
    while counter:
        time.sleep(delay)
        log.info("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

logger = logging.getLogger('thread_example')
logger.setLevel(logging.DEBUG)
    
db = {'host':'localhost', 'port': 3306, 'dbuser':'logger', 'dbpassword':'loggerpasswd', 'dbname':'logger'}

sqlh = mySQLHandler.mySQLHandler(db)
logger.addHandler(sqlh)

############## Basic Threads
logger.info("Entering Basic Threads")
# Create new threads
thread1 = myThread_basic(logger,1, "Thread-1-Basic", 1)
thread2 = myThread_basic(logger,2, "Thread-2-Basic", 2)

# Start new Threads
thread1.start()
thread2.start()

logger.info("Exiting Basic Tasks")

############## Synchronizing Threads

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread_sync(logger,1, "Thread-1-sync", 1)
thread2 = myThread_sync(logger,2, "Thread-2-sync", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
logger.info("Exiting Sync Tasks")
    
###### Multithreaded Priority Queue
logger.info("Entering Multithreaded Priority Queue")

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread_priorizedqueue(logger,threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
logger.info("Exiting Main Thread")
