import threading
import time
import logging

# A demo thread program to demonstrate a thread with events.
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s', )

def task(event):
    #threading.currentThread() FUNCTION determines the current thread
    logging.info("Starting the Task - %s"%(threading.currentThread().getName()))

    while not event.is_set():
        logging.info("waiting the event to be Set")
        time.sleep(2)
        logging.info("Sleeping for 2 seconds.")
    logging.info("######This is the event######")

def eventSetter(e):
    logging.info("%s will wait before 10 seconds before before setting the thread" %
                 (threading.currentThread().getName() ) )
    time.sleep(10)
    e.set()

if __name__ == "__main__":
    _e = threading.Event()
    _ts = threading.Thread(target=task, args=(_e,))
    _ev = threading.Thread(target=eventSetter, args=(_e,))

    _ts.start()
    _ev.start()
    _ts.join()
    _ev.join()
